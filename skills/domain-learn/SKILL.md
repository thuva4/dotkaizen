---
name: domain-learn
description: Use when learning from an existing domain knowledge base, preparing for domain discussions, testing domain understanding, or practising reasoning about domain scenarios and changes.
---

# Learn a domain from its evidence

Build understanding through explanations, realistic scenarios, and feedback. The knowledge base supplies evidence, not a guarantee of expertise.

## Orient

Before any canonical read, follow [read memory](../domain-work/references/read-memory.md), including catalogue discovery, snapshot checks, and freshness.

Select the organisation or context before reading substantive notes. Find the domain at `~/.domains/<domain-slug>/`, expanding `~` to the user's home directory. Discover candidates through `~/.domains/index.md`, falling back to immediate domain indexes. Match its scope, not its name alone; ask if ambiguous. If absent, report the missing knowledge base rather than creating facts or a local replacement.

Read the index's scope status, coverage, relevant pages, and questions. Load only topics needed for the goal. Infer the learner's role and starting point; ask if unclear and consequential.

Describe supported knowledge, dates, scope, and gaps. Apply the reader's freshness checks to claims about current behaviour. A review date does not make old evidence current. Scope confirmation does not verify domain facts. If a boundary or business-rule ambiguity changes the lesson's conclusion, ask a focused question; otherwise continue with its provisional scope explicit. Do not silently repair facts.

## Teach

Explain the purpose, important terms, actors, rules, and one end-to-end workflow. Give supported reasons for rules; identify missing rationale.

Trace responsibilities and workflows across systems before explaining the local service. Compare legacy, deployed new, and intended behaviour. Distinguish observed, configured, tested, and approved behaviour. Cite domain pages and source entries for factual claims.

Choose an edge case relevant to the learner's goal. Trace what is known about each system and where the evidence ends. Separate general background and explicitly hypothetical examples from verified behaviour. Unknown fallback, retry, migration, or rollback behaviour must remain unknown; neighbouring system behaviour does not establish it.

For proposed changes, examine affected rules, actors, dependencies, and edge cases. Treat impact analysis as reasoning to verify. Show stakeholder perspectives without treating seniority as evidence.

## Check understanding

Ask one useful scenario or teach-back question, then wait for the learner's answer before giving its solution. If the user explicitly requests a worksheet with answers, provide that format instead.

After the answer, assess the reasoning against cited evidence. Explain mistakes and uncertainty, then choose a follow-up question or reading. Distinguish demonstrated understanding from material merely presented. Do not award expert status after a lesson or invent answers, completion, or assessment results.

## Record only when requested

Default to teaching in conversation. If saving is requested, use `~/.domains/<domain-slug>/learning.md`, or an existing learning-notes page within that global domain directory. Label it as a personal learning record rather than domain facts.

Before any mutation, follow [storage and recovery](../domain-work/references/storage-and-recovery.md). Acquire the global directory lock, preserve raw recovery copies, re-read the learning record, then save and snapshot the coherent update.

Record the date, learning goal, cited materials, topics presented, actual answers, feedback, and next gaps. If the learner has not answered, record assessment as pending, not complete. Label hypotheticals clearly. Keep learning notes outside the established domain explanation.

New evidence or discovered factual corrections require an explicit knowledge-base update task. For a lesson, surface unresolved questions in conversation or the learning record; do not silently change current state, target state, or source claims.
