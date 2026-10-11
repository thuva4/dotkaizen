# Maintain scoped domain knowledge

## Scope and investigation

Compare the request with the index's organisation, purpose, workflows, inclusions, exclusions, and neighbours. A matching name or shared service is insufficient. Record scope changes explicitly.

If alternatives would change domain selection, edited files, or the requested conclusion, ask one focused question. Identify a known owner or relevant human role when evidence cannot establish business policy or responsibility. Do not contact them without authorization. Continue independent work within a provisional scope; leave dependent conclusions unresolved. Do not request approval again for an explicit scope already supplied.

Use the user's investigation limit. Otherwise state a first pass limited to the changed workflow and named sources. Stop when the question is supported, that limit is reached, or progress needs missing evidence or a consequential decision. Record inspected, inconclusive, inaccessible, and uninspected boundaries in the existing coverage table, with the next check and relevant revisions. Do not perform a blanket repository scan or claim a completeness percentage.

## Decide what changes

| Evidence | Update |
| --- | --- |
| Later state for the same scope | Replace current account; retain dated historical evidence |
| Different region or cohort | Update that scope; preserve other supported scopes |
| Unresolved contradiction | Record competing claims in questions; qualify affected summaries |
| Demonstrated error | Retract the false claim from current explanations; retain correction evidence |
| Proposed or approved change | Update intended behaviour; keep current behaviour separate |

Preserve supported parts of disputed claims. Label stale accounts historical or verification-needed until checked. Keep unsupported inferences as hypotheses outside established explanations. Include decision impact and the evidence needed to resolve questions.

## Trace drift

Search the changed source ID and affected terms within the selected domain. Check citing summaries, workflows, contracts, and edge cases, including legacy/new coexistence, migration, and rollback where relevant. Read source-register sections on demand rather than loading every record.

Keep previous revisions or source records needed to interpret historical claims. New citations must identify the changed revision; never silently retarget historical citations to new content. Preserve stable IDs, relative links, and unrelated edits.

Record implications for other domains as follow-up work with links and gaps. Do not claim those domains or downstream systems were checked unless actually inspected within the task scope.

## Write conservatively

Follow [storage and recovery](../../domain-work/references/storage-and-recovery.md) for every mutation. Use the global atomic directory lock and local Git snapshots, including catalogue and pending changes. Parallel agents may return read-only findings. A writer must acquire the lock before re-reading and modifying shared files. If acquisition fails, defer changes and report the unsaved handoff.

Immediately before writing, re-read affected files and compare them with planning versions. Reconcile intervening changes or defer. Allocate IDs from the current register and deduplicate evidence. Preserve unrelated edits and historical citations. Check affected links and explanations, commit a coherent snapshot, then release only the owned lock.

For task-start retrieval, on-use freshness, and finish reconciliation, follow [the memory lifecycle](../../domain-work/references/memory-lifecycle.md). Check relevant pending entries and resolve those incorporated into the update. Report interruptions and uncommitted changes explicitly. Local snapshots are recoverable versions, not a guarantee against disk failure or editors that ignore the protocol.
