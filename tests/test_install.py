"""Check install/sync behaviour on a copy of the repo with a temporary HOME.

Run: python3 tests/test_install.py
"""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent


def run(repo, home, harness):
    env = {**os.environ, "HOME": str(home)}
    out = subprocess.run([sys.executable, "-I", "build.py", "install", harness],
                         cwd=repo, env=env, capture_output=True, text=True, check=True).stdout
    return [line for line in out.splitlines() if not line.startswith(("dist/", "next:"))]


with tempfile.TemporaryDirectory() as tmp:
    repo, home = Path(tmp) / "repo", Path(tmp) / "home"
    shutil.copytree(SRC, repo, ignore=shutil.ignore_patterns(".git", "dist", "__pycache__"))
    agents = home / ".claude/agents"

    first = run(repo, home, "claude")
    assert all(line.startswith("installed:") for line in first) and len(first) >= 6, first
    assert run(repo, home, "claude") == [], "rerun with no changes must do nothing"

    # Model change in harnesses.json reaches unedited agents only.
    (agents / "judge.md").write_text((agents / "judge.md").read_text() + "\nlocal note\n")
    config = json.loads((repo / "harnesses.json").read_text())
    config["claude"]["fast"], config["claude"]["reviewer"] = "sonnet", "sonnet"
    (repo / "harnesses.json").write_text(json.dumps(config))
    second = run(repo, home, "claude")
    assert f"updated: {agents / 'explore.md'}" in second, second
    assert any("edited locally" in line and "judge.md" in line for line in second), second
    assert "model: sonnet" in (agents / "explore.md").read_text()
    assert "local note" in (agents / "judge.md").read_text()

    # An agent removed from the repo is removed from the install.
    (repo / "agents" / "explore.md").unlink()
    assert f"removed: {agents / 'explore.md'}" in run(repo, home, "claude")
    assert not (agents / "explore.md").exists()

    # A skill the user already had is never touched.
    own = home / ".config/opencode/skills/skill-evolve"
    own.mkdir(parents=True)
    (own / "SKILL.md").write_text("mine")
    opencode = run(repo, home, "opencode")
    assert (own / "SKILL.md").read_text() == "mine"
    # Skills managed under ~/.claude/skills are reused, not duplicated for opencode.
    assert not (home / ".config/opencode/skills/domain-work").exists(), opencode

print("install checks passed")
