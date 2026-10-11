# Compare skill behaviour and cost

The [evaluation pack](../evaluation.md) provides 12 fixed tasks, synthetic fixtures, scoring rules, and a per-run measurement format. It is a test dependency only; installed domain skills remain self-contained as a set.

Run D1–D6 to check recall, historical evidence, conflicts, cross-service reasoning, committed reads, and task continuation. Use W6 to produce the continuation input for D6. For D5, prepare the held-lock fixture exactly as specified in the pack. Run each variant in a fresh session against an unchanged isolated copy, with an explicit test-only knowledge-root override. Do not change the real home directory or use personal notes.

Compare a frozen current version with one candidate change at a time. Keep model, effort, available tools, sources, permissions, and context budget fixed. Start with three repetitions per case and variant. Record all results, including incomplete runs. A multi-change package comparison must be labelled as such and cannot identify which change caused a difference.

Alongside the pack's correctness, citation, time, and cost measurements, record:

- Which skill references and sections were actually read.
- Whether the answer preserved source revisions, time, region, and evidence type.
- Whether any unverified pending or partial-worktree claim entered the answer.
- Whether read-only file lists, hashes, HEAD, and lock metadata stayed unchanged.
- Whether continuation preserved the user's scope and verification status.

For the short recall route, the expected instruction reads are `domain-work/SKILL.md`, `read-memory.md`, and `direct-recall.md`. A runtime may independently load unrelated global instructions; record that overhead separately. Instruction word counts measure text size only. They do not measure runtime token consumption or cost.

Run the existing mutation and recovery scenarios when changing writer rules. Moving reader instructions must preserve committed-snapshot handling, no-HEAD handling, and re-reading before writes. Keep native skill activation and model routing checks separate from prompt-level evaluations.

Use [validation notes](validation.md) for actual observations. A planned case is not a passed test. Make cost claims only from actual runtime telemetry and include all participating agents.
