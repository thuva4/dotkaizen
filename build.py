"""Render agents/*.md into harness-specific files under dist/<harness>/.

Usage: python3 build.py [claude|codex|opencode ...]   (default: all)
       python3 build.py install <claude|codex|opencode>
Models per tier come from harnesses.json; edit it for the target machine.
install builds, then syncs agents and skills into the harness's user
directories under $HOME. Rerun it after editing agents/, skills/, or
harnesses.json. It records what it installed in ~/.dotkaizen/installed.json
and only updates or removes copies that are unchanged since it wrote them;
local edits and files it did not install are skipped with a message.
"""
import hashlib
import json
import shutil
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).parent

CLAUDE_TOOLS = {
    "read": "Read, Grep, Glob",
    "review": "Read, Grep, Glob, Bash",
    "build": "Bash, Read, Grep, Glob",
}
CODEX_SANDBOX = {"read": "read-only", "review": "read-only", "build": "workspace-write"}
OPENCODE_PERMISSION = {
    "read": """  edit: deny
  bash: deny
  webfetch: deny
  task: deny""",
    "review": """  edit: deny
  webfetch: deny
  task: deny
  bash:
    "*": ask
    "git diff*": allow
    "git log*": allow
    "git show*": allow
    "git -C * rev-parse *": allow
    "git -C * show *": allow
    "git -C * log *": allow
    "ls *": allow
    "grep *": allow""",
    "build": """  edit: deny
  webfetch: deny
  task: deny
  bash:
    "*": ask
    "mvn *": allow
    "./mvnw *": allow
    "gradle *": allow
    "./gradlew *": allow
    "grep *": allow
    "tail *": allow
    "head *": allow
    "ls *": allow
    "find * -name *": allow""",
}


def load(path):
    _, front, body = path.read_text().split("---\n", 2)
    meta = dict(line.split(": ", 1) for line in front.strip().splitlines())
    for key in ("name", "description", "mode", "tier", "access"):
        assert key in meta, f"{path}: missing {key}"
    return meta, body.strip() + "\n"


def claude(meta, body, models):
    # A primary agent omits `tools` to inherit everything; run it with `claude --agent <name>`.
    tools = "" if meta["mode"] == "primary" else f"tools: {CLAUDE_TOOLS[meta['access']]}\n"
    return f"agents/{meta['name']}.md", (
        f"---\nname: {meta['name']}\ndescription: {meta['description']}\n"
        f"model: {models[meta['tier']]}\n{tools}---\n{body}"
    )


def codex(meta, body, models):
    if meta["mode"] == "primary":
        return "instructions.md", "## Coordinate a task\n\n" + body
    text = (
        f"name = {json.dumps(meta['name'])}\ndescription = {json.dumps(meta['description'])}\n"
        f"model = {json.dumps(models[meta['tier']])}\n"
        f"model_reasoning_effort = {json.dumps(meta.get('effort', 'medium'))}\n"
        f"sandbox_mode = {json.dumps(CODEX_SANDBOX[meta['access']])}\n"
        f'developer_instructions = """\n{body}"""\n'
    )
    tomllib.loads(text)  # fail the build on invalid TOML
    return f"agents/{meta['name']}.toml", text


def opencode(meta, body, models):
    if meta["mode"] == "primary":
        subagents = sorted(m["name"] for m, _ in AGENTS if m["mode"] == "subagent")
        perm = '  task:\n    "*": deny\n' + "".join(f"    {n}: allow\n" for n in subagents)
    else:
        perm = OPENCODE_PERMISSION[meta["access"]] + "\n"
    steps = f"steps: {meta['steps']}\n" if "steps" in meta else ""
    return f"agents/{meta['name']}.md", (
        f"---\ndescription: {meta['description']}\nmode: {meta['mode']}\n"
        f"model: {models[meta['tier']]}\n{steps}permission:\n{perm}---\n{body}"
    )


AGENTS = [load(p) for p in sorted((ROOT / "agents").glob("*.md"))]
RENDER = {"claude": claude, "codex": codex, "opencode": opencode}
# Per harness, relative to $HOME: agent dir, then skill dirs it scans (installs into the first).
TARGETS = {
    "claude": (".claude/agents", [".claude/skills"]),
    "codex": (".codex/agents", [".agents/skills", ".codex/skills"]),
    "opencode": (".config/opencode/agents", [".config/opencode/skills", ".claude/skills", ".agents/skills"]),
}
NEXT = {
    "claude": "start sessions with `claude --agent orchestrator`",
    "codex": "append dist/codex/instructions.md to ~/.codex/AGENTS.md if it is not there yet",
    "opencode": "switch to the orchestrator agent with Tab or `opencode --agent orchestrator`",
}


def build(name, harnesses):
    shutil.rmtree(ROOT / "dist" / name, ignore_errors=True)  # drop files for removed agents
    for meta, body in AGENTS:
        rel, text = RENDER[name](meta, body, harnesses[name])
        out = ROOT / "dist" / name / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(text)
        print(out.relative_to(ROOT))


def digest(path):
    """Content hash of a file or a directory tree; None if absent."""
    if not path.exists():
        return None
    files = sorted(p for p in path.rglob("*") if p.is_file()) if path.is_dir() else [path]
    h = hashlib.sha256()
    for f in files:
        h.update(str(f.relative_to(path)).encode() if path.is_dir() else b"")
        h.update(f.read_bytes())
    return h.hexdigest()


def put(src, dest):
    if dest.is_dir():
        shutil.rmtree(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    (shutil.copytree if src.is_dir() else shutil.copy2)(src, dest)


def install(name):
    manifest_path = Path.home() / ".dotkaizen" / "installed.json"
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    agents_rel, skills_rel = TARGETS[name]
    agents_dir, scanned = Path.home() / agents_rel, [Path.home() / d for d in skills_rel]
    wanted = [(f, [agents_dir / f.name]) for f in sorted((ROOT / "dist" / name / "agents").iterdir())]
    wanted += [(d, [s / d.name for s in scanned]) for d in sorted((ROOT / "skills").iterdir()) if d.is_dir()]

    for src, candidates in wanted:
        # Prefer a copy this tool manages, then any existing copy the harness scans, then its own dir.
        dest = next((c for c in candidates if str(c) in manifest),
                    next((c for c in candidates if c.exists() or c.is_symlink()), candidates[0]))
        current, recorded, new = digest(dest), manifest.get(str(dest)), digest(src)
        if current is None and not dest.is_symlink():
            put(src, dest)
            print(f"installed: {dest}")
        elif recorded is None:
            print(f"skip, not installed by this tool (compare and update by hand): {dest}")
            continue
        elif current != recorded:
            print(f"skip, edited locally since install (merge by hand, or delete it and rerun): {dest}")
            continue
        elif current != new:
            put(src, dest)
            print(f"updated: {dest}")
        else:
            continue
        manifest[str(dest)] = new

    # Remove agents this tool installed for this harness that the build no longer produces.
    produced = {str(agents_dir / f.name) for f in (ROOT / "dist" / name / "agents").iterdir()}
    for path in [p for p in manifest if Path(p).parent == agents_dir and p not in produced]:
        if digest(Path(path)) in (manifest[path], None):
            Path(path).unlink(missing_ok=True)
            print(f"removed: {path}")
            del manifest[path]
        else:
            print(f"skip removal, edited locally: {path}")

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, indent=1, sort_keys=True) + "\n")
    print(f"next: {NEXT[name]}")
    print("next: check model IDs in harnesses.json against this machine, then restart the harness")


if __name__ == "__main__":
    harnesses = json.loads((ROOT / "harnesses.json").read_text())
    if sys.argv[1:2] == ["install"]:
        assert len(sys.argv) == 3 and sys.argv[2] in RENDER, "usage: build.py install <claude|codex|opencode>"
        build(sys.argv[2], harnesses)
        install(sys.argv[2])
    else:
        for name in sys.argv[1:] or RENDER:
            build(name, harnesses)
