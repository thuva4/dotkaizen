# Pilot log

Two weeks of real work before adding or changing instructions. The goal is to find out which roles earn their cost, then delete the rest. Record wrong behaviour in `failures.local.md` (template: [failures.md](failures.md)); record every task here, including ones where delegation did not happen.

## Setup

Fill in once, and again if anything changes mid-pilot.

- Start date:
- Machine and harness:
- Repository commit (`git rev-parse --short HEAD`):
- Models from `harnesses.json` (fast / strong / reviewer):
- Other plugins or skills active:
- Domain built for the pilot (`~/.domains/<slug>`):

## Plan

- Week 1: orchestrator, explore, and tester on real tasks. Separately, build one real domain with domain-build.
- Week 2: add domain-reader and judge's domain check on tasks that depend on business rules.
- Do not edit agents or skills during the pilot unless a failure blocks work. If you must, note the new commit here.

## Tasks

One row per task. Delegated: agents actually called, with counts, for example `explore×2, tester×1`. Helped: `yes`, `no`, or `partial`, judged by you. Wrong: an F-number from failures.md, or blank. Tokens: total for the task from the harness's usage view, including subagents; `unknown` if unavailable.

| Date | Task (one line) | Harness / model | Delegated | Helped | Wrong | Tokens | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | |

## Review at the end

Count from the table, then decide. Deleting a role is a valid result.

| Role or feature | Calls | Helped | Wrong | Keep, change, or delete |
| --- | --- | --- | --- | --- |
| explore | | | | |
| tester | | | | |
| judge (code review) | | | | |
| judge (domain check) | | | | |
| domain-reader | | | | |
| lesson candidates | | | | |
| domain candidates | | | | |

Starting thresholds; adjust them before the pilot starts, not after:

- Fewer than five calls in two weeks: delete the role or feature, or make it on-request only.
- Wrong more often than helpful: change it through failures.md and skill-evolve, or delete it.
- Tasks with delegation cost clearly more tokens than similar tasks without it, with no quality gain: narrow the delegation rule.
- domain-reader briefs that misjudge scope: keep `tier: strong`; if still wrong, let the orchestrator ask you instead.

Record the decisions, then make each change as its own commit.
