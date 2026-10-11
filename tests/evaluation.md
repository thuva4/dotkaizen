# Repeatable workflow evaluation

Use this pack to compare agent instructions on the same tasks. The fixtures are synthetic. Keep live repositories, accounts, installed agents, and real domain memory outside the trial.

## Run a comparison

1. Freeze the current instructions as variant A. Make one change for variant B. Record file hashes or commits, runtime, model, reasoning effort, tool availability, and date. To measure the whole package, label it a combined comparison; it cannot isolate one change's effect.
2. Choose cases below before running. Use an unchanged copy of [the fixtures](fixtures/refunds/sources.md) for every run. Give the executing agent only the selected task, fixture paths, and relevant role or skill instructions. Keep this rubric out of its context.
3. Use a fresh session for each case and repetition. Run three repetitions per variant for an initial pilot, alternating A/B order. Keep tools, model, effort, permissions, sources, and context budget the same. If a setting cannot be held constant, record the difference. Do not treat a simulated role prompt as a test of native agent discovery or routing.
4. Save the exact prompt, answer, tool trace, timestamps, configuration, fixture hash, and file changes under a chosen results directory. For read-only cases, compare fixture file lists and hashes before and after. Use an isolated memory root override for domain cases; never repoint the real home directory.
5. Score each result against the acceptance criteria. Inspect citations and any programmatic flags manually. Report every run, including failures and incomplete runs. A small pilot detects regressions; it does not establish statistical reliability.

## Cases and acceptance criteria

For code cases, use the `fixtures/refunds/` directory. For domain cases, apply `domain-work` from `skills/domain-work/`. A domain-memory fixture can use this pack's S1 as its saved historical note, with an Acme merchant-refund index and source register. State the isolated root explicitly in the task. Freeze that fixture for both variants.

| ID | Role / mode | Task to give the agent | Acceptance criteria for the evaluator |
| --- | --- | --- | --- |
| W1 | explore | Locate the retry-key retention boundary and Orders retry scheduling/reuse logic. | Finds both files, explains the relevant observations with line references, and states the inspected scope. Does not propose a fix. |
| W2 | explore | Locate provider-side duplicate suppression in these excerpts. | Reports the scoped absence of evidence, names what was searched, and avoids claiming the provider has no suppression. |
| W3 | judge | Review `boundary.diff` against the supplied contract and code. | Identifies the exact-expiry mismatch, with trigger, consequence, and source/line evidence. |
| W4 | judge | Review `rename.diff` against the supplied contract and code. | Finds no demonstrated defect in the equivalent comparison. States material verification limits without inventing a finding. |
| W5 | coordinator | The supplied equivalent-expression diff was reviewed and its required checks passed on this revision. No changes followed. Decide the next action. | Completes the task without another automatic review. Does not claim to have personally run supplied checks. |
| W6 | coordinator | Prepare a continuation handoff from `handoff-input.md`; do not write files. | Preserves the goal, read-only constraint, completed reads, source revisions, unrun tests, unresolved provider behaviour, next action, and completion condition. |
| D1 | direct recall | What retry window does pay-r3 specify, why was it chosen, and is it deployed in the US? | Answers five minutes with evidence. Keeps rationale and pay-r3 US deployment unknown. Preserves the historical scope of S1/S3. No memory writes or quiz. |
| D2 | direct recall | What retention did pay-r2 specify on 2026-09-01? | Answers 15 minutes for that revision and date. Does not replace the historical answer with S2. |
| D3 | direct recall | Does the supplied evidence show everyone uses v2? | Distinguishes the unsupported S5 assertion from S3 configuration and measured exposure. Does not claim current global deployment. |
| D4 | read-only investigation | Can an Orders retry after 20 minutes rely on the supplied Payments retention window? | Compares 1,200 and 300 seconds, preserves key reuse, and leaves provider behaviour/deployment unresolved. No invented end-to-end guarantee. |
| D5 | direct recall | Repeat D1 while another synthetic writer holds a lock and has written an unsupported 999-minute worktree claim. | Reads saved memory from one committed snapshot, excludes the partial claim, uses supplied S2, and leaves notes, HEAD, lock, and owner unchanged. |
| D6 | task continuation | Resume from the W6 handoff using the same fixtures and read-only constraint. | Continues at the missing provider evidence, preserves scope and unrun-test status, and avoids repeating completed exploration without a new reason. |

For D5, the evaluator initializes and commits only the isolated memory fixture, then creates the synthetic lock and partial edit. Record the commit before the agent starts. Do not run D5 against personal notes. An unversioned fixture with a held lock needs a separate expectation: dependent memory conclusions are deferred because no committed snapshot exists.

## Measurements

Record one row per case, variant, and repetition:

```text
case, variant, repetition, model, effort, runtime, instruction_revision,
fixture_revision, outcome, supported_claims, checked_claims,
missed_required_items, unsupported_findings, redundant_reads,
tool_calls, elapsed_seconds, input_tokens, cache_read_tokens,
cache_write_tokens, output_tokens, cost, notes
```

Use `pass`, `fail`, or `incomplete` for outcome. Citation support is supported factual claims divided by checked factual claims; use unavailable when the denominator is zero. Count a repeated read as redundant only when it adds no new scope, revision, consistency check, or necessary verification. A reviewer must inspect this judgement. Code locations alone do not establish a supported explanation.

Obtain token counts and cost from actual runtime telemetry. Record unavailable when telemetry is absent. Do not estimate these from word counts or subagent self-reports. Record the pricing source and date if calculating cost from token use. Include the coordinator and all child calls when measuring a delegated workflow; a child-only measurement cannot establish total savings.

Record cache reads and writes separately from uncached input; they are priced differently. For a delegated run, also note the coordinator's cache writes on its first call after each child returns. A spike there means its cache expired while it waited, for example during a long test run.

## Decide what to keep

Compare correctness and missed evidence first, then median and range of time and cost. Report false review findings separately. Preserve failures rather than averaging them away. If a cheaper variant misses consequential evidence, revise it before adopting it. When results disagree across tasks, keep the choice conditional on the task type.

### Held-in, held-out, and retention

Cases written from [failures.md](failures.md) are held-in: they motivated a change. W1–W6 and D1–D6 are held-out: never edit them, or add cases to that set, to make a candidate pass. Keep a candidate only if its held-in case passes and no held-out or earlier held-in case regresses. Rerun the full set, not only the new case. You decide what to keep from these results; an agent's opinion of its own change does not count. Tag each kept revision, for example `skills-v3`, so later versions can be compared against it.

### Protect the evaluator

A candidate change must not modify `tests/`, fixtures, or acceptance criteria in the same commit. Record fixture hashes before and after each run and discard runs where they changed. Change cases in a separate, reviewed commit and rerun the current frozen version on them before comparing a candidate.

### Prune

Use the recorded instruction reads from real tasks as well as eval runs. A reference or section unread or without effect across ten real tasks is a deletion candidate. Remove it as an ordinary candidate change: the full set must not regress.

Test prompt changes with a fixed model first. A later model or effort comparison is a separate experiment. Instructions alone do not establish that the runtime installed or selected the intended agent.
