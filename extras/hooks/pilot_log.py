#!/usr/bin/env python3
"""Claude Code SessionEnd hook: append one row per session to tests/pilot-log.md.

Reads the hook payload (JSON with transcript_path, session_id, cwd) on stdin and
fills the countable columns: date, task (first prompt), model, delegated agents,
tokens. Helped and Wrong stay blank for the human. A resumed session updates its
existing row instead of adding a second one.

Log path: $PILOT_LOG, else tests/pilot-log.local.md in this repo (gitignored, so
real entries never reach the remote). A missing log is created from the tracked
template tests/pilot-log.md.
Never fails the session: errors go to stderr and the exit code is 0.
"""
import collections
import fcntl
import json
import os
import re
import sys
import tempfile
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
TEMPLATE = REPO / "tests" / "pilot-log.md"
DEFAULT_LOG = REPO / "tests" / "pilot-log.local.md"
TAG_BLOCK = re.compile(r"<([a-z][\w-]*)[^>]*>.*?</\1>", re.S)
EMPTY_ROW = re.compile(r"^\|(\s*\|)+\s*$")


def read_jsonl(path):
    entries = []
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                try:
                    entries.append(json.loads(line))
                except ValueError:
                    continue
    except OSError:
        pass
    return entries


def prompt_text(entry):
    """Return the human-typed text of a user entry, or '' for tool results and wrappers."""
    if (entry.get("type") != "user" or entry.get("isMeta") or entry.get("isSidechain")
            or entry.get("isCompactSummary")):
        return ""
    content = entry.get("message", {}).get("content")
    if isinstance(content, list):
        if any(c.get("type") == "tool_result" for c in content if isinstance(c, dict)):
            return ""
        content = " ".join(c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text")
    if not isinstance(content, str):
        return ""
    text = " ".join(TAG_BLOCK.sub(" ", content).split())
    return "" if text.startswith("[Request interrupted") else text


def usage_total(entries):
    """Sum tokens over assistant messages, counting each message id once."""
    seen, total = set(), 0
    for e in entries:
        if e.get("type") != "assistant":
            continue
        msg = e.get("message", {})
        mid = msg.get("id") or e.get("uuid")
        if mid in seen:
            continue
        seen.add(mid)
        u = msg.get("usage") or {}
        total += sum(int(u.get(k) or 0) for k in (
            "input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"))
    return total


def summarise(transcript_path):
    entries = read_jsonl(transcript_path)
    if not any(e.get("type") == "assistant" for e in entries):
        return None
    task = next((t for t in map(prompt_text, entries) if t), "(no prompt)")
    models = collections.Counter(
        e["message"].get("model") for e in entries
        if e.get("type") == "assistant" and e.get("message", {}).get("model") not in (None, "<synthetic>"))
    agents = collections.Counter()
    tool_tokens = 0
    for e in entries:
        msg = e.get("message", {})
        if e.get("type") == "assistant" and not e.get("isSidechain"):
            for c in msg.get("content") or []:
                if isinstance(c, dict) and c.get("type") == "tool_use" and c.get("name") in ("Agent", "Task"):
                    agents[(c.get("input") or {}).get("subagent_type") or "general-purpose"] += 1
        result = e.get("toolUseResult")
        if isinstance(result, dict) and isinstance(result.get("totalTokens"), int):
            tool_tokens += result["totalTokens"]

    tokens = usage_total(e for e in entries if not e.get("isSidechain"))
    sub_dir = Path(transcript_path).with_suffix("") / "subagents"
    sub_files = sorted(sub_dir.glob("*.jsonl")) if sub_dir.is_dir() else []
    sidechain = usage_total(e for e in entries if e.get("isSidechain"))
    if sub_files:
        sub_tokens = sum(usage_total(read_jsonl(f)) for f in sub_files)
    else:
        sub_tokens = sidechain or tool_tokens
    note = ""
    if agents and not sub_tokens:
        note = "subagent tokens not found; main only"

    stamps = [e.get("timestamp") for e in entries if e.get("timestamp")]
    try:
        date = datetime.fromisoformat(stamps[0].replace("Z", "+00:00")).astimezone().date().isoformat()
    except (IndexError, ValueError):
        date = datetime.now().date().isoformat()
    return {
        "date": date,
        "task": task if len(task) <= 90 else task[:87] + "...",
        "model": models.most_common(1)[0][0] if models else "unknown",
        "delegated": ", ".join(f"{k}×{v}" for k, v in sorted(agents.items())) or "none",
        "tokens": tokens + sub_tokens,
        "note": note,
    }


def cell(text):
    return str(text).replace("|", "\\|").replace("\n", " ").strip()


def build_row(info, session_id, project):
    notes = "; ".join(x for x in (f"auto: session {session_id[:8]}, {project}", info["note"]) if x)
    cols = [info["date"], info["task"], f"Claude Code / {info['model']}", info["delegated"],
            "", "", f"{info['tokens']:,}", notes]
    return "| " + " | ".join(cell(c) for c in cols) + " |"


def upsert(lines, row, session_id):
    """Replace this session's row or append after the last row of the Tasks table."""
    marker = f"session {session_id[:8]}"
    start = next(i for i, l in enumerate(lines) if l.strip() == "## Tasks")
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
    table = [i for i in range(start, end) if lines[i].startswith("|")]
    if len(table) < 2:
        raise ValueError("Tasks table not found")
    for i in table[2:]:
        if marker in lines[i]:
            lines[i] = row
            return lines
    for i in reversed(table[2:]):
        if EMPTY_ROW.match(lines[i].strip()):
            del lines[i]
    # Indices shifted after deletions: find the table's last line again from the separator.
    last = table[1]
    while last + 1 < len(lines) and lines[last + 1].startswith("|"):
        last += 1
    lines.insert(last + 1, row)
    return lines


def main():
    payload = json.load(sys.stdin)
    transcript = payload.get("transcript_path")
    session_id = payload.get("session_id") or Path(transcript or "x").stem
    if not transcript or not os.path.exists(transcript):
        return
    info = summarise(transcript)
    if info is None:
        return
    log = Path(os.environ.get("PILOT_LOG") or DEFAULT_LOG)
    project = Path(payload.get("cwd") or ".").name
    row = build_row(info, session_id, project)
    with open(str(log) + ".lock", "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        source = log if log.exists() else TEMPLATE
        lines = source.read_text(encoding="utf-8").splitlines()
        text = "\n".join(upsert(lines, row, session_id)) + "\n"
        mode = (log.stat().st_mode & 0o777) if log.exists() else 0o644
        fd, tmp = tempfile.mkstemp(dir=log.parent, prefix=".pilot-log.")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as fh:
                fh.write(text)
            os.chmod(tmp, mode)
            os.replace(tmp, log)
        except BaseException:
            if os.path.exists(tmp):
                os.unlink(tmp)
            raise


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:  # a logging hook must never break session shutdown
        print(f"pilot_log hook: {exc}", file=sys.stderr)
    sys.exit(0)
