"""Check the SessionEnd pilot-log hook on a synthetic transcript and a temporary log.

Run: python3 tests/test_pilot_log.py
"""
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent
HOOK = SRC / "extras/hooks/pilot_log.py"


TEMPLATE = """# Pilot log

## Tasks

| Date | Task (one line) | Harness / model | Delegated | Helped | Wrong | Tokens | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

## Review at the end

| Role or feature | Calls |
| --- | --- |
| explore | |
"""


def assistant(mid, content, usage, model="claude-opus-5-5"):
    return {"type": "assistant", "timestamp": "2026-10-11T10:00:00Z",
            "message": {"id": mid, "model": model, "content": content, "usage": usage}}


def run(log, transcript, session="abcdef1234"):
    payload = json.dumps({"session_id": session, "transcript_path": str(transcript),
                          "cwd": "/x/myproj", "hook_event_name": "SessionEnd"})
    res = subprocess.run([sys.executable, "-I", str(HOOK)], input=payload, text=True,
                         capture_output=True, env={**os.environ, "PILOT_LOG": str(log)})
    assert res.returncode == 0 and not res.stderr, res.stderr
    return log.read_text().splitlines()


def rows(lines):
    start = lines.index("## Tasks")
    return [l for l in lines[start:] if l.startswith("| 2026")]


with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    log = tmp / "pilot-log.md"
    log.write_text(TEMPLATE)
    before = log.read_text()
    use = {"input_tokens": 10, "output_tokens": 5, "cache_creation_input_tokens": 100, "cache_read_input_tokens": 1000}
    entries = [
        {"type": "user", "timestamp": "2026-10-11T10:00:00Z",
         "message": {"content": "<system-reminder>ignore me</system-reminder>Fix the a|b parser\nplease"}},
        assistant("m1", [{"type": "tool_use", "name": "Agent", "input": {"subagent_type": "explore"}}], use),
        assistant("m1", [{"type": "text", "text": "same message, second block"}], use),
        {"type": "user", "message": {"content": [{"type": "tool_result", "content": "found"}]}},
        assistant("m2", [{"type": "tool_use", "name": "Agent", "input": {"subagent_type": "explore"}},
                         {"type": "tool_use", "name": "Agent", "input": {"subagent_type": "tester"}}], use),
    ]
    transcript = tmp / "abcdef1234.jsonl"
    transcript.write_text("\n".join(json.dumps(e) for e in entries))
    subdir = tmp / "abcdef1234" / "subagents"
    subdir.mkdir(parents=True)
    (subdir / "agent-1.jsonl").write_text(json.dumps(assistant("s1", [], {"input_tokens": 7, "output_tokens": 3})))

    lines = run(log, transcript)
    got = rows(lines)
    assert len(got) == 1, got
    row = got[0]
    assert "Fix the a\\|b parser please" in row and "ignore me" not in row, row
    assert "explore×2, tester×1" in row, row
    assert "2,240" in row, row  # 2 unique messages × 1115 + 10 subagent tokens
    assert "session abcdef12, myproj" in row and "claude-opus-5-5" in row, row
    assert not any(l.strip().replace(" ", "") == "|||||||||" for l in lines), "placeholder row kept"

    # Resumed session: same id updates its row, does not add a second one.
    entries.append(assistant("m3", [], {"output_tokens": 60}))
    transcript.write_text("\n".join(json.dumps(e) for e in entries))
    got = rows(run(log, transcript))
    assert len(got) == 1 and "2,300" in got[0], got

    # A second session appends below the first.
    other = tmp / "other.jsonl"
    other.write_text("\n".join(json.dumps(e) for e in entries[:2]))
    got = rows(run(log, other, session="9999999999"))
    assert len(got) == 2 and "session 99999999" in got[1] and "explore×1" in got[1], got

    # Empty session (no assistant reply) leaves the log alone; other sections are untouched.
    empty = tmp / "empty.jsonl"
    empty.write_text(json.dumps(entries[0]))
    after = log.read_text()
    assert run(log, empty, session="0000000000") == after.splitlines()
    assert after.split("## Tasks")[0] == before.split("## Tasks")[0]
    assert after.split("## Review at the end")[1] == before.split("## Review at the end")[1]

    # A missing log is created from the tracked template, which stays unchanged.
    fresh = tmp / "new" / "pilot-log.local.md"
    fresh.parent.mkdir()
    template = (SRC / "tests/pilot-log.md").read_text()
    got = rows(run(fresh, transcript))
    assert len(got) >= 1 and "session abcdef12" in got[-1], got
    assert (SRC / "tests/pilot-log.md").read_text() == template

    # Placeholder above a hand-added row: new row must stay inside the table (judge finding 1).
    manual = tmp / "manual.md"
    manual.write_text(TEMPLATE.replace("| | | | | | | | |\n", "| | | | | | | | |\n| 2026-10-10 | manual | CC | none | yes | | 5 | |\n"))
    os.chmod(manual, 0o644)
    lines = run(manual, transcript)
    sep = lines.index("| --- | --- | --- | --- | --- | --- | --- | --- |")
    assert lines[sep + 1].startswith("| 2026-10-10") and "session abcdef12" in lines[sep + 2], lines
    assert lines[sep + 3] == "" and lines[sep + 4] == "## Review at the end", lines
    assert oct(manual.stat().st_mode & 0o777) == "0o644", "file mode changed"
    assert not list(tmp.glob(".pilot-log.*")), "temp file left behind"

    # Interrupt markers and compaction summaries are not taken as the task.
    noisy = tmp / "noisy.jsonl"
    noisy.write_text("\n".join(json.dumps(e) for e in [
        {"type": "user", "isCompactSummary": True, "message": {"content": "This session is being continued"}},
        {"type": "user", "message": {"content": "[Request interrupted by user]"}},
        {"type": "user", "message": {"content": "Real task here"}},
        assistant("n1", [], use)]))
    got = rows(run(log, noisy, session="5555555555"))
    assert "Real task here" in got[-1], got

print("pilot_log hook: ok")
