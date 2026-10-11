---
name: domain-work
description: Use for factual or historical business-domain questions, or when explicitly asked for persistent domain-memory work. Not for general coding tasks.
---

# Use domain memory during work

Use domain memory to answer the question or support the requested project task. Explicit read-only requests take precedence.

## Choose the mode

For question-only requests, read [read memory](references/read-memory.md) and [direct recall](references/direct-recall.md), answer with evidence, then stop. These are the required recall references. Load write or recovery procedures only after an explicit save/update request. Do not start a quiz. Recall does not authorize persistence, even when supplied evidence corrects the notes.

For exploration, design, coding, review, or an explicit save/update request, use work mode. This authorizes supported note maintenance within the task scope. Combined questions and project changes use work mode unless the user requests read-only work.

## Before work mode

Before any canonical read, follow [read memory](references/read-memory.md), including catalogue discovery, snapshot checks, and freshness. Read [memory lifecycle](references/memory-lifecycle.md) for reconciliation and task handoffs. Select domains through `~/.domains/index.md` and verify each selected domain's own scope.

Ask only when competing domain identities change the work. State the decision-relevant facts, their dates and scopes, and remaining gaps. Apply the reader's source checks before relying on current operational claims.

If memory is absent, continue evidence-based project work. Use domain-build for an authorized initial map. If material scope is unknown, ask one focused question and continue independent work. Do not invent a domain taxonomy to unblock the task.

## During work

Keep the project task primary. Trace relevant handoffs within a bounded pass. Record candidate discoveries with locators, revisions, scope, evidence type, and affected pages. Separate observations, requirements, proposals, and unknowns.

For a multi-step task, keep its goal, current step, and completion condition explicit. Update task state when progress changes. At a context handoff, use the lifecycle's task-state format so completed reads and verification need not be reconstructed.

At a substantial milestone or before a context handoff, reconcile supported findings. Save unresolved candidates in the domain's `pending.md` only when needed for continuation. They are not established facts. Do not save every conversation or duplicate existing sources.

Read [storage and recovery](references/storage-and-recovery.md) before any memory mutation. Use its global writer lock and local Git snapshots. All four skills share this protocol. Do not hold the lock during source investigation or user questions.

## Before finishing

Use domain-update to reconcile evidence into affected explanations, source records, questions, and coverage. Initial mapping uses domain-build. Read the applicable skill in full; do not infer its instructions from its name. Preserve valid history and cross-service scope. Uninspected neighbouring domains receive follow-up links, not unsupported changes.

Update the global catalogue when identity, aliases, relationships, or service mappings change. Clear or resolve reconciled pending entries. Unchanged evidence requires no new source or commit. Learning records remain opt-in through domain-learn.

Report the project result, memory files changed, snapshot commit, material unknowns, and next check. If a lock, missing tool, interruption, or read-only request prevents persistence, say exactly what remains unsaved and provide a concise handoff. Do not claim reconciliation succeeded when only a proposal was produced.

If the user corrected how you applied these skills, or a check failed because of a skill rule, end the report with one lesson candidate: skill and section, what happened, the user's words or the failing check, and the evidence. Report it only; do not edit skills or record it yourself. Skill lessons are not domain facts.

This skill is active when invoked or selected by persistent instructions. It cannot guarantee execution in sessions that do not load it, source-change notifications, or recovery from disk loss.
