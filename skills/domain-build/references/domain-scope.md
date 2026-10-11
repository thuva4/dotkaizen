# Establish domain scope

Use a useful, evidence-backed model. Do not assume there is one perfect domain taxonomy.

## Identify the domain

Start from the user's business question, organisation or operating context, and outcome. Trace one or two representative workflows: their trigger, end condition, actors, key concepts, rules, and decisions. Compare the meaning of shared words across workflows. A service, repository, team, shared entity, or technical dependency does not by itself define a domain.

Before reusing notes, compare their organisation, purpose, included workflows, and exclusions with the request. Similar names do not establish identical meaning. Link neighbouring or overlapping domains instead of silently merging them. Distinguish capability scope from the systems currently implementing it.

## Record the scope in index.md

Use a short `Domain scope` section:

- Organisation or operating context, domain name, and aliases.
- Purpose, business outcomes, principal actors, and representative workflows.
- Included responsibilities and explicit exclusions.
- Neighbouring domains, shared contracts, and handoff points.
- Status: provisional or scope-confirmed; evidence or human confirmation, date, and remaining boundary questions.

Scope confirmation does not verify all domain facts or establish complete coverage. Use explicit scope already supplied by the user rather than asking again. Do not invent confirmation or ownership.

## Human decisions

The agent proposes the boundary with evidence, alternatives, and exclusions. If competing scopes would change the domain selected, files changed, or requested conclusion, ask one focused question. This includes material expansion, splitting, merging, or business-rule and ownership conflicts that the evidence cannot resolve.

Identify the human role or known owner who could resolve a consequential business question, and the precise decision needed. Do not contact them without authorization. The user can confirm the investigation scope; that confirmation alone does not establish another team's policy or ownership.

Continue supported exploration within a clearly provisional scope when uncertainty is nonblocking. Keep dependent conclusions unresolved. Ordinary reads and supported updates within the agreed scope do not need repeated human approval.

## Limit the investigation

Use the user's investigation limit. Otherwise state a first pass covering one representative workflow and a short named source set. Use targeted searches and reads. Follow handoffs only far enough to answer the question; record remaining branches rather than scanning the whole enterprise.

Stop the pass when the question is supported, its stated limit is reached, or progress needs missing evidence or a consequential human decision. Report why it stopped and the next useful check. Do not claim that unsearched code is absent or that one successful trace covers every path.

Keep a small coverage table in the index or system map:

| Workflow or responsibility | Inspected systems and evidence | Status | Gap or next check |
| --- | --- | --- | --- |

Distinguish reviewed, inspected-but-inconclusive, inaccessible, and uninspected areas. Record relevant revisions and a continuation point so a later session can resume without repeating the entire search. Use section-based reads for large registers. Do not invent a completeness percentage.
