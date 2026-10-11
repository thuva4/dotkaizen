# Discover, retrieve, reconcile, and revisit

All paths are under the user's expanded `~/.domains/`. Keep knowledge as Markdown. Git supplies local versions; no database, daemon, hooks, or connector is required. Use [read memory](read-memory.md) for discovery, consistent snapshots, and freshness. Load this lifecycle for work mode or an authorized update.

## Global catalogue

Keep `~/.domains/index.md` small:

```markdown
# Domains

| Domain | Organisation / context | Outcome and exclusions | Aliases | Services / repositories | Related domains | Scope status |
| --- | --- | --- | --- | --- | --- | --- |
| [Library loans](library-loans/index.md) | Example Library | Lend items to members; excludes purchases | borrowing, checkouts | catalogue, circulation, notifications | [Membership](membership/index.md), separate process | Provisional |
```

This row is an example, not seed knowledge. Create entries only for actual domains. Domain indexes remain authoritative for scope. Catalogue relationships identify overlap, dependency, or separate meanings; they do not establish ownership or verified integration.

Recover missing catalogue entries under the writer lock. Catalogue changes follow the same storage procedure as other canonical writes.

For a task spanning domains, identify each domain and the handoff being examined. Maintain only the explicitly selected scopes. Consequential merge, split, ownership, or policy decisions need evidence or human input. Shared entities and services are insufficient grounds for a merge.

## Reconcile source changes

Changed content requires a new versioned source record and targeted searches of citing summaries, workflows, contracts, and edge cases. Do not retarget historical citations. Unchanged content retains its original observation date and needs no timestamp-only update. For an authorized substantive update, record the actual check and a concrete next trigger, such as a rollout change, contract revision, or named decision. There is no background monitoring.

## Reconciliation and handoff

At a meaningful milestone and task completion, classify each candidate:

| Candidate | Destination |
| --- | --- |
| Supported new fact or correction | Source register and affected scoped explanations |
| Proposed or approved design | Target state, with approval status and evidence |
| Conflict or consequential missing evidence | Open questions, linked from relevant explanations |
| Incomplete investigation worth resuming | `pending.md`, with status clearly unverified |
| Existing evidence with no changed conclusion | No duplicate record |

A pending entry contains a stable task ID, question, candidate claim, exact locator/revision, scope, what was actually checked, reason pending, affected pages, and next action. Missing fields say unknown. Do not copy pending claims into factual summaries. Re-read existing entries and deduplicate by source, scope, and question. Resolved entries link the resulting source or question before removal or brief archival.

If persistence is unavailable, return the pending entry in conversation. Do not write around a held lock to another shared file. At the next session, read relevant pending entries alongside the index. Use an explicit checkpoint before context compaction when possible; interrupted conversations without a checkpoint can still lose discoveries.

## Task handoff

At a context handoff, preserve this compact task state:

- Goal, selected domain, source boundary, and user constraints, including read-only status.
- Completed work and inspected files or symbols, with their revisions.
- Decisive evidence, source locators, and unresolved claims.
- Verification actually run, its command/result and revision; checks not run and why. Label supplied results separately from your own execution.
- Current step, changed or unsaved files, next action, and completion condition.

Keep this state in conversation for read-only work. During authorized memory work, include it with a relevant `pending.md` entry only when continuation needs persistence, using the full writer protocol. Task status is not domain knowledge. Reuse completed work on resumption, then recheck evidence or verification when sources, code, constraints, or required scope changed. Do not turn the handoff into a transcript archive.
