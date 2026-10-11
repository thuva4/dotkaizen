# Answer a domain question

Use this mode when the requested result is an answer: a rule, workflow explanation, historical decision, comparison, or source lookup. Follow [read memory](read-memory.md) before discovery, then read only the relevant evidence. Pending entries and raw recovery copies are not established facts. Recall needs neither the writing lifecycle nor the mutation/recovery procedure.

Resolve material domain ambiguity with one focused question. Otherwise answer within the stated scope. If the domain or evidence is absent, say what is missing. Do not build a knowledge base to answer a question.

## Answer contract

Lead with the supported answer. Add nearby links to the relevant domain page and precise source entry or original source. State the revision, date, environment, or cohort when it changes the answer. Keep implementation, deployment, approved intent, and observation distinct. Cite supplied new evidence directly when it has no saved source ID; never invent a register entry or source ID.

Explain a decision's reason only when evidence records it. Implementation reveals a mechanism, not necessarily its business rationale. If reasons, rejected alternatives, approval, or ownership are undocumented, say so. Label any requested inference explicitly.

For historical questions, answer from evidence for that time and scope. A later contract does not invalidate what an older version specified. For current operational questions, apply [decision-relevant freshness](read-memory.md#check-decision-relevant-freshness) using available read-only sources. Respect requests to use notes only. If current evidence cannot be checked, answer with the dated account and make current applicability unknown.

Mention material contradictions and unknowns near the answer. Search only far enough to answer the question or reach the stated source limit. Do not turn a short lookup into an enterprise investigation.

## Stop after answering

Do not quiz, save learning progress, update check dates, repair the catalogue, write pending entries, acquire a writer lock, initialize Git, or commit. Report a discovered correction briefly in conversation, with its evidence and the fact that it is unsaved. An explicit request to save or correct notes switches to work mode and domain-update; it does not authorize unrelated changes. Use domain-learn only when teaching, practice, or assessment is requested.

Example: old notes describe a 14-day loan renewal period at lib-r2. A supplied lib-r3 excerpt specifies seven days but gives no reason or deployment record. Answer that lib-r3 specifies seven days; explain that its rationale and deployment are unknown; cite the excerpt; identify the old notes as lib-r2. Keep both revisions unchanged on disk.
