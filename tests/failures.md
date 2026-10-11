# Skill and agent failures

Raw experience for improving instructions. Add an entry when a task ends with a lesson candidate you agree with, or when you notice a failure yourself. Entries are evidence, not rules. A change reaches a skill or agent only through a held-in eval case and the comparison in [evaluation.md](evaluation.md).

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

### F1 — 2026-10-11 — orchestrator / delegation to tester and judge

- File: `agents/orchestrator.md`
- Task: blog post rewrite plus seven new SVG animation modules (~2,000 lines) and new scene data contracts in a personal site repo; Claude Code, orchestrator as main session, Opus.
- What happened: no subagent was started in the whole session. Builds and Playwright runs of 2–6 minutes were run directly with output trimmed to `tail -1` or a pass/fail count, which let them count as "short checks". No judge review ran on the new modules; the report said "no independent review". Two modules shipped without their `mount()` call and were caught only by screenshots. The Claude Code Agent tool's own rule ("do not spawn agents unless the user asks") also overrode the delegation instructions.
- Expected: long runs go to tester regardless of how much output is shown; new modules and new data contracts get a judge review before the work is reported done.
- Evidence: user asked "did orchestrator used sub agents, why the skills where not triggered. What do we need to change?"; session transcript shows zero Agent calls; `~/.claude/settings.json` has `"agent": "orchestrator"`.
- Status: fixed by request, without an eval case: the tester and judge paragraphs now carry measurable triggers (over 60 seconds or long output, trimming does not count, browser runs count; judge required for a new or changed data contract, a new file over ~150 lines, or a behaviour change across more than three files). The Agent-tool conflict needs a standing permission in the user's instruction file, which dotkaizen does not install.
