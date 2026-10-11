# Validation notes

Initial validation date: 2026-10-10. Second-brain revision: 2026-10-11.

## Initial structural checks

- All three skills pass the bundled skill-creator `quick_validate.py` check.
- Each `SKILL.md` is under 600 words and has a distinct name and description.
- All actual local Markdown links resolve. Inline code examples are excluded from link checks.
- The repository contains no application code, executable helpers, or runtime dependencies. PyYAML was used from a temporary directory to run the existing validator; it was not added to the project.

## Execution checks

Independent agents applied the initial skills to synthetic fixtures in a temporary directory. The parent reviewed the generated files and teaching response. These were separate executions, not self-assessments of the skill text. They predate the global-storage revision; the storage revision is checked separately below.

### domain-build

Produced seven navigable pages. Preserved EU 10%, US 0%, and legacy-default configuration scope. Kept approved idempotency, merged deduplication, and the observed legacy incident distinct. Put unresolved rollout and duplicate-prevention assertions on the questions page, linked from the index. Recorded exact excerpt locators, review dates, missing original records, and inaccessible Wiki access.

### domain-update

Updated the regional account to EU 100%, US 0%, and US legacy default, within the deployment excerpt's scope. Preserved the earlier rollout as history and kept the all-region target separate from actual rollout. Maintained the unresolved product-note conflict and checked affected summaries and edge cases.

The evaluating agent applied the same sources a second time. All seven file hashes were unchanged: no duplicate sources, questions, or history. The parent reviewed the resulting regional descriptions, target, history, and unresolved questions.

### domain-learn

Identified missing v2 failure and fallback evidence. Distinguished the legacy incident from unknown v2 behaviour. Asked a hypothetical recovery question without providing its solution or simulating an answer. Declined to certify expertise after one lesson.

Saved only a labelled personal learning record, with assessment pending. The parent compared all seven pre-existing domain page hashes: none changed. The hypothetical was labelled, and no learner answers or completion were invented.

## Global-storage revision

An independent agent read the revised skills and README, then planned paths for build, update, and saved learning from three different service repositories. All selected `~/.domains/refunds/`; saved learning selected its `learning.md`. The dry run did not access or write the real global directory.

It also checked ambiguous company-specific domains and existing project-local documentation. It identified an unspecified update path when the canonical knowledge base is absent. The update skill now explicitly reports that absence and asks whether to build first. The build skill now specifies lowercase, hyphenated business names for new domains. Existing local documentation remains source material, with no automatic move or deletion.

A focused follow-up confirmed that build creates the canonical global directory, update asks whether to build the missing base, and learn reports its absence. None moves the project-local source documents.

Frontmatter, local links, whitespace, and the global-path instruction in each skill were checked after the revision. This is a path-planning check, not a new execution of the original evidence scenarios.

## Limits

The initial revision received one execution scenario per skill, followed by the focused checks described here. These checks establish observed handling of these fixtures, not general factual accuracy, statistical reliability, or live connector compatibility. No real Slack, Atlassian, or GitHub account was accessed. Additional scenarios in `scenarios.md` are suggested future checks unless covered explicitly above or below.

To repeat the checks, create isolated fixtures from `scenarios.md`, ask a fresh agent to apply one skill, and inspect the actual files and response against that scenario's criteria. Keep the update scenario's ADR independent from the build fixture. Check repeated updates by comparing file hashes and source/question counts.

## Enterprise-use revision

GPT-6 Astra at high effort reviewed the original revision and the revised skill text. Findings and disposition are in [the review](../../docs/enterprise-review.md). Text review alone does not establish execution behaviour.

A separate pre-revision dry run handled several boundary, retention, and investigation questions correctly through general judgement. It proposed re-reading an intervening edit and allocating a new ID, but did not establish a single writer while another session was active. This baseline is one observation, not a measured performance comparison.

### Bounded build and domain expansion

A fresh agent applied the revised build skill to three synthetic contract excerpts in an isolated temporary directory. It created four Markdown pages, combining related concepts and workflows rather than forcing empty files. The parent inspected the generated scope, coverage table, source locators, workflow, and questions.

The index recorded the user-supplied merchant-refund investigation boundary, explicit exclusions, scope-confirmation limits, inspected revisions, uninspected neighbours, the three-source pass limit, stop reason, and continuation. No complete enterprise map or deployed behaviour was claimed.

When asked to add compensation, replacements, and store credit and assign ownership, the agent retained the existing supported scope, recorded the unresolved expansion, and asked whether to model an umbrella capability or merged domain. It did not invent combined ownership or remedy rules.

### Retention decision

The build evaluator read an applicable synthetic policy prohibiting personal-directory retention of restricted incident contents and derived facts. It did not read the incident contents or persist them. It rejected the requested save and did not assume redaction permitted retention or silently choose another canonical location. This was a policy-handling dry run, not an enterprise permission test.

### Intervening edit and contract drift

A fresh agent read a six-page synthetic domain and planned a payments-contract update without writing. The parent then appended source S8 and an independent US configuration finding. That controlled writer finished before the evaluating agent resumed.

The resumed update re-read the files, preserved S8 and the regional paragraph exactly, and allocated S9 for the revised payments contract. It updated the index, implementation description, workflow, retry edge case, sources, and questions. The old S5 revision remained interpretable. Ledger compatibility, deployment, and accounting effects stayed unverified.

The parent inspected all six pages and checked preservation of the intervening content, source identities, revised citations, and local links. This simulates an intervening edit; it does not test live race exclusion or prove transactional behaviour. The evaluator stated it would coordinate or defer if the other writer were still active.

### Learning with a consequential scope gap

A revised-skill dry run asked for a confirmed explanation of replacement goods and combined ownership while the supplied domain excluded those remedies. The agent explained the supported refund path, identified the separate workflow and unknown ownership, asked which scope to investigate, and declined to mark unsupported claims confirmed. It made no writes or global reads. This checked the response to a consequential boundary gap, not a completed lesson or persisted learning record.

### Remaining validation limits

No large real codebase, live connector, multi-user enterprise store, long-running maintenance period, or actual concurrent race was tested. No cost or completeness percentage was measured. Use a controlled personal pilot, with human review of consequential domain decisions, before making enterprise reliability claims.

## Second-brain revision

Earlier sections describe their own revisions. The checks below apply to the four-skill lifecycle and storage revision. Access and retention checks were excluded at the user's request. No real global notes, installed skills, persistent agent instructions, or external source accounts were changed.

### Baseline

A separate agent read the previous three-skill set. It identified missing operational procedures for global discovery, automatic task-start/finish reconciliation, recoverable versions, and active writer detection. Source drift and manual source-aware updates were present, but freshness checks before design had to be inferred. The baseline made no writes.

### Discovery, freshness, and reconciliation

An independent agent applied domain-work in an isolated temporary home with two differently scoped refund domains. The requested Acme domain was absent from the global catalogue but present on disk. Notes cited a 24-hour implementation contract. A supplied revised contract specified 15-minute retention, without deployment or neighbouring-service evidence.

The execution selected Acme through immediate-index fallback, repaired its catalogue row, retained the other organisation, registered S2 without changing S1's historical meaning, and updated five affected Markdown pages. It correctly rejected safe deduplication as an assumption after 20 minutes, kept deployment and Ledger compatibility unknown, and identified the unsupported prior Orders handoff. It committed the coherent update and released its lock. An unrelated user file stayed untracked and unchanged. The parent inspected all changed content and commit scope.

A repeated execution using the revised storage instructions made no changes, duplicate sources, timestamp-only edits, or new commit. HEAD and tracked files remained unchanged; no recovery checkpoint was needed for a no-op.

### Lock primitive and committed reader

The parent launched two local `mkdir` processes against the same absent lock directory. Exactly one acquired it. A separate initialization fixture checked root-local Git, ignored lock state, pinned committed reads during an incomplete worktree edit, and a file-scoped restore.

A fresh agent used a fixture with an externally held lock and an unsupported 999-minute claim in its worktree. It read canonical memory from one pinned commit, rechecked the actual source excerpts, and retained the supported 15-minute conclusion. Its acquisition attempt failed. The parent confirmed the external owner, partial file, HEAD, and unrelated file remained unchanged.

A further held-lock execution supplied genuinely new pay-r3 evidence. The agent reported the five-minute implementation finding and returned a complete unsaved handoff in conversation. It did not write a pending entry around the lock, modify canonical notes, or change HEAD. The parent confirmed the controlled owner and partial worktree remained unchanged.

### Failed publication

A separate fixture supplied a five-minute implementation contract and a configured synthetic rejecting pre-commit hook. The evaluating agent saved exact raw copies of all five affected files, updated sources and scoped explanations, checked the staged diff, and attempted an actual commit. The hook rejected it.

No commit was published. The agent preserved staged changes, raw copies, Git settings, the hook, and unrelated content. It retained its owned lock with an explicit interruption note and reported the unpublished paths. The parent inspected the actual copies, staged blobs, unchanged HEAD, owner notice, and unrelated file.

### Interrupted recovery execution

After the parent repaired the synthetic hook externally, the evaluating agent received an explicit request to complete the interrupted update. It inspected and preserved the unfinished contents in a second raw checkpoint, retained its existing lock ownership, validated the staged tree, and published a new coherent commit. Both checkpoints remained available. The parent checked the actual commit, unchanged configuration and hook, unchanged unrelated file, clean tracked status, and released lock. No hook, signing, or identity setting was bypassed.

### First-commit recovery primitives

The parent separately exercised an initial commit rejection with no HEAD. It preserved original content and absent-file records, copied interrupted files to another checkpoint, removed only affected staging, restored the original file, removed a task-created absent-before file, and released the owned lock after recovery. Interrupted contents remained available in raw copies. This was a command-level procedure check, not an independent agent recovery trial.

### Current structural checks and limits

All four skill entrypoints pass the bundled skill-creator validator and remain below 600 words. Actual local Markdown links and anchors resolve. Whitespace checks pass. The repository adds no executable helpers or runtime packages; the documented storage protocol uses standard filesystem operations and Git.

These are controlled synthetic executions, not measurements of large-codebase completeness, missed dependencies, factual accuracy over time, live connector behaviour, cost, crash durability, or human learning outcomes. Cooperating local writers were tested; arbitrary editors and shared/network filesystems were not. Persistent activation is supplied as a README instruction, not installed or guaranteed. Independent backup remains outside the local Git mechanism.

## Direct recall and activation revision: 2026-10-11

### Baseline and execution

A separate baseline agent read the prior domain-work instructions. For a question-only request with a new five-minute contract excerpt, it correctly identified missing rationale and deployment, but concluded that invocation mandated persisting the new evidence. The old skill authorized maintenance without distinguishing an answer-only request.

After the mode split, a fresh agent applied the revised skill to an actual isolated home. The question asked for the supplied contract's retry window, rationale, and US deployment. Saved notes described pay-r2's 15-minute window. Another controlled writer held the lock and had written an unsupported 999-minute worktree claim. The supplied pay-r3 source specified five minutes, with no rationale or deployment evidence.

The agent selected direct recall, answered five minutes with a direct source citation, kept rationale and US deployment unknown, and identified saved pay-r2 evidence as historical. It used a pinned committed snapshot for memory and did not use the partial worktree. It reported the new finding as unsaved, asked no quiz question, and performed no writer action.

The parent compared actual Markdown hashes and file sets, HEAD, owner metadata, and the partial worktree. All were unchanged. No pending entry was created. This verifies observed read-only recall under these fixture conditions; it does not establish general retrieval accuracy.

### Activation documentation

Installation and instruction locations were checked against official Codex and Claude Code documentation linked in the README. Codex's documented user skill path for new installation is `~/.agents/skills/`; the README now uses it and explains checking older copies before installing duplicates. Global instruction locations and Codex override precedence are explicit. Claude Code verification distinguishes `/context` for loaded instructions from `/memory` for file locations.

The parent executed the README copy block with both destinations replaced by temporary directories. All four skills and their references were copied for each runtime. A repeat skipped all eight existing targets and preserved a deliberately added local edit. No actual installation, global instruction change, hook configuration, or real knowledge-base access occurred.

No hook is required for the documented baseline. The README describes optional startup/compaction reminders and their limited purpose without adding a runtime script or settings change. Actual application discovery, persistent activation, and real-domain retrieval quality remain part of the user's pilot.
