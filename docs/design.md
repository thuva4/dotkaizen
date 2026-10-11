# Domain knowledge skills

## Purpose

Help one person understand unfamiliar domains and reason about changes using a small, maintained Markdown knowledge base. The same skills work across domains and stakeholders.

## Agreed scope

Create four skills: `domain-work`, `domain-build`, `domain-update`, and `domain-learn`. Store them in this repository. Keep the implementation to Markdown files. Source access uses available tools or supplied exports; the skills do not install connectors, run background jobs, or publish changes to source systems.

Store domain knowledge globally at `~/.domains/<domain-slug>/`, shared across services and projects. Select domains by business scope rather than repository names. Project documentation contributes evidence and links to the canonical domain explanation. Never move existing project documentation automatically.

## Knowledge model

- Separate observed current behaviour from proposals, approved intentions, and implementation or rollout in progress.
- Cover legacy systems, deployed new components, and their coexistence. A system can be current for one cohort and intended for another.
- Attach scoped source evidence to factual claims. Record source dates, revisions, locators, and access limits.
- Evaluate evidence for the claim being made, not the seniority of its author. A decision record can establish intent; a production record can establish a rollout within its scope.
- Keep unresolved claims and contradictions in a clearly separate questions page. Preserve established facts that remain supported.
- Describe edge cases using triggers, behaviour by system, transition effects, evidence, and unknowns.
- Keep one canonical explanation per topic. Split pages only when needed for readability.
- Map responsibilities and end-to-end workflows across services, repositories, teams, and external systems. Assess coverage against workflows and boundaries; keep missing access and unexplored dependencies visible.

## Skill boundaries

| Skill | Input | Result |
| --- | --- | --- |
| domain-work | Domain question or exploration, design, coding, or review task | Read-only cited recall, or scoped retrieval and supported work reconciliation |
| domain-build | Domain scope and available source material | A navigable knowledge base and explicit evidence gaps |
| domain-update | Existing knowledge base and new evidence or a refresh request | Targeted edits, preserved provenance, and impact notes |
| domain-learn | Existing knowledge base and a learning goal | Evidence-based explanations, scenarios, and feedback |

Install all four sibling skill directories together. Each SKILL.md defines its task boundary. The build skill has page-format and domain-scope references; update has maintenance guidance; domain-work supplies shared lifecycle and storage references. The README provides usage, optional installation, and a persistent-instruction snippet. It does not silently change global agent instructions.

The shared `read-memory.md` reference owns snapshot selection, scoped discovery, and freshness checks. Direct recall loads this reader and its answer contract. Work mode adds lifecycle guidance; mutations add storage and recovery guidance. All four skills use the reader before canonical discovery. Task handoffs retain execution state separately from domain facts.

Question-only requests select direct recall. They produce a supported answer with citations, time and system scope, and material unknowns. They do not authorize persistence, quizzes, or repair of discovered discrepancies. Supplied new evidence can change the answer while saved notes remain unchanged. Work mode applies to project tasks and explicit save or update requests. Learning remains a separate opt-in task.

The README supplies current Codex and Claude Code installation paths, non-overwriting copy instructions, global and project activation locations, an instruction block, and a fresh-session behaviour check. No hook is required for the initial pilot. Optional event reminders can be considered if the pilot demonstrates missed activation; they cannot replace evidence-aware reconciliation.

## Enterprise-use safeguards

Propose business boundaries from representative workflows and record them in the index, with scope status and evidence. Human input is needed for consequential identity, boundary, policy, or ownership ambiguity; supported exploration can continue within a provisional scope. Confirmation of scope does not certify facts or completeness.

Use bounded investigation passes with visible coverage and continuation points. Check changed source IDs and terminology across affected pages. Preserve old source revisions for historical claims. Use one global atomic directory lock for all canonical mutations, re-read before writing, and reconcile intervening changes. Preserve raw pre-edit copies outside factual retrieval, then publish coherent local Git snapshots after checking the staged tree. Readers use a pinned committed snapshot during writes. Recovery handles failed initial commits and absent-file records. Access and retention review is excluded from this revision at the user's request.

These are Markdown workflows for a controlled personal pilot. They coordinate cooperating local writers but do not protect against tools that ignore the protocol, crash-atomic writes, incomplete discovery, or unseen source changes. Freshness is checked on use. Local history is not a disk-loss backup.

## Validation

Check skill frontmatter and relative links. Exercise the skills on synthetic source conflicts, partial rollout updates, and unknown outage behaviour. Inspect the resulting Markdown and check that unsupported claims are not promoted to facts. Structural validation does not prove factual correctness or complete source coverage.
