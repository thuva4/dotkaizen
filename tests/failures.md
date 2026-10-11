# Skill and agent failures

Raw experience for improving instructions. This file is the template: keep your entries in `tests/failures.local.md`, which is gitignored so they never reach the remote (copy this file there to start). Add an entry when a task ends with a lesson candidate you agree with, or when you notice a failure yourself. Entries are evidence, not rules. A change reaches a skill or agent only through a held-in eval case and the comparison in [evaluation.md](evaluation.md).

Look for repeated patterns before proposing a change. A single entry rarely justifies one.

## Entry format

```markdown
### F<n> — <yyyy-mm-dd> — <skill or agent> / <section>

- File: repo-relative path of the instruction, for example `agents/judge.md` or `skills/domain-work/SKILL.md`.
- Task: what was being done, project, harness, and model.
- What happened: the behaviour, quoted or summarized from the transcript.
- Expected: what should have happened, and why.
- Evidence: user's words, failing check output, or transcript locator.
- Status: open | eval case <id> | fixed in <tag> | rejected (<reason>)
```

## Entries

Add entries in `tests/failures.local.md`, not here.
