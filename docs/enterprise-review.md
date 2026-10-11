# Enterprise-use review

Reviewer: GPT-6 Astra, high effort. Date: 2026-10-10. Reviewed commit: `62b6070`.

The sections through the second review record that earlier revision. The current second-brain review is recorded below.

## Assessment

The initial skills are a useful foundation for a personal, evidence-based domain notebook. Their evidence distinctions are sound. They do not establish enterprise-wide completeness or enforce safe concurrent writes.

## Findings

| Priority | Finding | Failure mode |
| --- | --- | --- |
| P1 | Domain identity lacks a discovery method | Merchant refunds and customer compensation share a name but have different rules; an agent merges them |
| P1 | Global persistence lacks retention rules | Readable restricted information is copied into personal notes without permission to retain it there |
| P1 | Shared files have no writer protocol | Two sessions assign the same source ID or overwrite each other's changes |
| P2 | Investigation lacks a stopping rule | A dependency trace expands through a large codebase without answering the original question |
| P2 | Consequential ambiguity has no escalation rule | A visible open question still leads to an unsupported design conclusion |
| P2 | Cross-repository drift checks are underspecified | A changed contract is corrected in one page but remains stale in workflows or edge cases |
| P2 | Validation is limited | Small synthetic examples do not establish enterprise reliability, cost, or connector compatibility |

The findings concern `domain-build/SKILL.md` domain selection and exploration, `domain-update/SKILL.md` coordinated edits and tracing, and the build page format's boundaries and source metadata. They were checked against the reviewed files before revision.

## Human involvement

The agent should propose a scoped, provisional model using business outcomes and representative workflows. Service and team boundaries are evidence about responsibilities, not automatic domain boundaries. There is no requirement to discover one perfect taxonomy.

Human input is needed when materially different domain identities would change the work, when unresolved business rules affect the requested conclusion, or when ownership, authority, or applicable retention rules cannot be established from evidence. Ordinary source reads, supported updates, and exploration within a stated provisional scope do not require repeated approval. Do not contact stakeholders without authorization.

## Reliability limit

Markdown guidance can reduce errors and support a controlled personal pilot. It does not enforce access control, transactions, complete discovery, or freshness. Real enterprise trials are needed to measure missed dependencies, unsupported or stale claims, correction effort, reviewer agreement, and investigation cost.

`~/.domains/` shares notes across projects for one user's home directory. It is not a shared enterprise service across users.

## Revisions and second review

The build skill now reads a domain-scope guide for business workflow discovery, explicit scope records, human decisions, investigation limits, coverage, and continuation. The update skill reads maintenance guidance for consequential ambiguity, drift checks, historical evidence, and a single-writer protocol. All three skills check organisation or context and applicable retention rules. The README explains everyday use and the remaining limits.

Astra reviewed the revised text at high effort. It found no remaining blocker to a controlled personal pilot, while identifying two follow-ups: preserve applicable evidence from earlier tasks or other domains, and distinguish new validation from the earlier checks. The evidence-reuse wording was corrected. Known retention restrictions now require compliance; only material uncertainty requires clarification.

This second review checked text and design, not execution. Focused execution and dry-run checks are recorded separately in [validation notes](../tests/domain/validation.md). The enterprise reliability limit remains unchanged.

## Second-brain revision: 2026-10-11

The user excluded access and retention review from this revision. The active skills no longer impose those additional policy checks.

| Finding | Change |
| --- | --- |
| No global discovery procedure | Global catalogue with context, outcome, aliases, services, and domain links; immediate-index fallback |
| Retrieval and updates depend on separate prompts | domain-work wraps project work with start retrieval, milestone checkpoints, and finish reconciliation; README supplies optional persistent instructions |
| Freshness is only a date | Decision-relevant source comparison on use, with revision/scope checks and explicit unknown current applicability |
| No recoverable storage history | Raw pre-edit copies plus coherent published local Git commits; scoped normal and interruption recovery |
| Concurrent writers can race | Atomic global directory acquisition for cooperating writers; committed-snapshot reads during updates |
| Validation is text-heavy | Isolated actual discovery/update/repeat, contention, held-reader, failed-commit, and recovery checks |

GPT-6 Astra reviewed this revision at high effort. It found two P1 defects: consistent-reader instructions loaded after discovery, and raw baseline commits that could publish inconsistent content. Both were corrected: all four skills load reader rules before canonical reads, and raw checkpoints remain outside Git and factual retrieval.

A follow-up identified incomplete first-commit/stale-lock recovery and a need to validate the staged tree rather than the worktree. The storage guide now separates normal restore from interrupted recovery, handles no HEAD and absent-file records, preserves unrelated staging, and checks the tree that will be published. Astra confirmed these narrow corrections and reported no remaining blocker in them. This is a text-review result, not an enterprise reliability certification.

Execution evidence and its limits are recorded separately in [validation notes](../tests/domain/validation.md). Remaining limits include sessions that do not activate the skill, writers outside the protocol, unavailable evidence, interruptions before checkpoints, and disk loss. Local Git does not replace an independent backup. Long-running real-domain trials remain necessary.
