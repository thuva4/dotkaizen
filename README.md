# dotkaizen

Personal agent dotfiles with kaizen: harness-neutral agent roles, domain-memory skills, a continuous-improvement loop, and an evaluation pack. One canonical definition per role renders into Claude Code, Codex, and opencode files, or can be adapted by hand for any other harness.

## Layout

```text
agents/          Canonical roles: portable frontmatter + plain-Markdown prompt
skills/          Agent Skills (SKILL.md): domain-work, domain-build, domain-update, domain-learn, skill-evolve
harnesses.json   Model per tier for each harness; edit for the target machine
build.py         Renders agents/ into dist/<harness>/ (stdlib Python 3.11+)
extras/          Harness-specific settings snippets
docs/            Domain skills guide, design, and review
tests/           Evaluation pack, fixtures, failure log; tests/domain/ for domain-skill scenarios
```

## Roles

| Role | Mode | Tier | Access | Does |
| --- | --- | --- | --- | --- |
| orchestrator | primary | strong | full | Coordinates the task and delegates; its prompt is the coordination instructions |
| explore | subagent | fast | read | Locates code and returns cited observations with the search boundary |
| tester | subagent | fast | build | Runs the given build/test command; returns a failure summary, not the log |
| judge | subagent | reviewer | review | Reviews a diff or plan for demonstrated defects |
| domain-reader | subagent | strong | review | Answers one domain question from `~/.domains/`; returns a cited brief of at most ten claims |

Each `agents/*.md` file has this frontmatter:

- `name`, `description`: role identity and when to delegate to it.
- `mode`: `primary` runs the session; `subagent` is delegated to.
- `tier`: `fast`, `strong`, or `reviewer`. `harnesses.json` maps tiers to models. Prefer a reviewer from a different model family than the orchestrator, so review stays independent.
- `access`: `read` (no edits or shell), `review` (no edits; read-only git and grep), `build` (no edits; may run build tools), `full` (the main session).
- `effort`: optional reasoning effort, where the harness supports it.
- `steps`: optional cap on agent iterations; rendered for opencode only.

The body after the frontmatter is the role's prompt, with no harness-specific syntax.

## Build

```sh
python3 build.py              # all harnesses
python3 build.py opencode     # one harness
```

Output goes to `dist/<harness>/`, which is not committed. Edit `agents/` and `harnesses.json`, never `dist/`. The build fails on missing frontmatter fields or invalid Codex TOML.

Claude Code and opencode can run the main session as a custom agent, so the orchestrator renders as an agent file there. Codex custom agents are subagents only; its main session reads `AGENTS.md`, so the orchestrator renders to `dist/codex/instructions.md` to append there.

## Install

Check model IDs on the target machine first and edit `harnesses.json`. The defaults have not been tested against a specific account. Then run:

```sh
python3 build.py install claude      # or codex, opencode
```

It builds the harness files and copies the agents and all skills into that harness's user directories. Run the same command again to sync after editing `agents/`, `skills/`, or `harnesses.json`, or after pulling changes:

- Unchanged installed copies are updated; agents removed from the repository are removed.
- Copies you edited since install, and files the command did not install, are skipped with a message. Merge by hand, or delete the copy and rerun to take the new version.
- A skill already present in any directory the harness scans is reused, so installing for Claude Code and opencode on one machine does not list skills twice.

It records what it installed, with content hashes, in `~/.dotkaizen/installed.json`. It does not edit instruction files or settings; it prints the remaining steps. `python3 tests/test_install.py` checks this behaviour against a temporary home directory.

The per-harness notes below cover what the command does not do.

### Claude Code

- Check discovery with `/agents` after a restart.
- Start sessions as the orchestrator with `claude --agent orchestrator`, or set `"agent": "orchestrator"` in `~/.claude/settings.json` to make it the default. It inherits all tools and uses the `strong` model.
- Optionally merge `extras/claude-settings.snippet.json` into `~/.claude/settings.json`. Do not replace the whole file; preserve existing hooks, permissions, plugins, and environment entries. Its model names are version-specific.
- The Bash tool caps one command at 10 minutes. Scope long test suites, or tester reports a timeout.

### Codex

- Open a new session and request agents explicitly, for example "Use the tester agent to run `./gradlew :orders:test` and summarize failures."
- Append `dist/codex/instructions.md` to `~/.codex/AGENTS.md`, or the active `AGENTS.override.md`.
- explore and judge use a read-only sandbox. tester uses workspace-write because builds write to `target/` or `build/`; its network is blocked by default, so dependencies must be cached or network allowed for that run.
- This setup does not change your main Codex model, global subagent defaults, or compaction settings.

### opencode

- For one repository only, copy `dist/opencode/agents/*.md` into its `.opencode/agents/` instead.
- Switch to `orchestrator` with Tab or `--agent orchestrator`. It may delegate only to explore, tester, and judge.
- Model IDs use `provider/model`; run `opencode models` on that machine. Through OpenCode Zen, IDs start with `opencode/`.
- opencode has no sandbox. Read-only behaviour comes from each agent's `permission` block.

### Any other harness

Use `agents/*.md` directly:

1. Put the orchestrator body in the harness's main system prompt or instruction file (`AGENTS.md` is the most widely read).
2. Create a subagent for each other role with its body as the prompt, its `description` as the delegation hint, a model for its `tier`, and tool permissions matching its `access`.
3. If the harness has no subagents, keep the orchestrator instructions and run each role as a separate session with its body as the prompt.

To support it permanently, add a model map to `harnesses.json` and a render function to `build.py`.

Skills in `skills/` follow the Agent Skills format: a folder with `SKILL.md`. Claude Code reads `~/.claude/skills/`, Codex `~/.agents/skills/`, and opencode reads `~/.config/opencode/skills/` plus both of those. Install each skill in one location per machine to avoid duplicate listings.

## Domain memory

`domain-work`, `domain-build`, `domain-update`, and `domain-learn` keep evidence-based domain knowledge under `~/.domains/`, shared across projects. The [domain skills guide](docs/domain-skills.md) covers usage, the persistent-instruction snippet, and the knowledge-base layout.

- Gathering domain knowledge and executing tasks are separate. Use the domain skills directly to build, update, query, and learn a domain. The orchestrator, explore, and tester never load domain skills or read `~/.domains/`.
- When business rules matter, the orchestrator asks domain-reader one bounded question and receives a brief: at most ten claims with source IDs, dates, scope, evidence type, and unknowns. Domain notes stay in that short-lived subagent's context.
- judge reads `~/.domains/` through domain-work direct recall to verify a change independently. It never writes domain memory. A violated rule is a finding only when the rule is supported and its scope covers the change; stale or out-of-scope notes become questions.
- For changes heavy on business rules, judge reviews the plan before implementation, so rule conflicts surface before code is written.
- The orchestrator ends its report with domain candidates: facts the task established, with evidence. It never records them. Run domain-update yourself to save the ones you accept.
- domain-work's description and the instruction snippet trigger only on domain questions or explicit domain-memory requests, so coding sessions do not load it automatically.
- Lesson candidates about agents and skills go to [tests/failures.md](tests/failures.md), and skill-evolve proposes changes to any of them.

## Improve instructions from failures

Agents and domain-work end a report with a lesson candidate when you corrected them or a check failed because of an instruction. Add the ones you agree with to [tests/failures.md](tests/failures.md).

[skill-evolve](skills/skill-evolve/SKILL.md) reads that log, groups repeated failures by cause, and proposes one minimal edit and one held-in eval case per pattern. It does not apply changes. Edit `agents/` or the skill, rebuild, run the comparison in the evaluation pack, keep the change only if nothing regresses, then update the entry status.

## Pilot

Before changing instructions, use the harness on real work for two weeks and fill in the [pilot log](tests/pilot-log.md). Its end-of-pilot review decides which roles to keep, change, or delete.

## Evaluate changes

The [evaluation pack](tests/evaluation.md) supplies 12 repeatable cases, synthetic fixtures, scoring rules, and measurements. Compare one instruction change at a time with the same harness, model, effort, and tools. Measure total parent-and-child work before claiming delegation saves cost; delegation also adds tokens. Harness, model, and effort changes each need a separate comparison.

## Status

Prepared only. No harness configuration was changed. Rendered files are syntax-checked by the build. Native agent discovery, permissions, and model routing still need a pilot in each harness.

## Documentation

- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/model-config
- https://learn.chatgpt.com/docs/agent-configuration/subagents
- https://learn.chatgpt.com/docs/config-file/config-reference
- https://opencode.ai/docs/agents/
- https://opencode.ai/docs/skills/
- https://opencode.ai/docs/rules/
