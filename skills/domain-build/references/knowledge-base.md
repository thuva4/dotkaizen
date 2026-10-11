# Markdown knowledge-base format

Store each domain at `~/.domains/<domain-slug>/`, shared across projects. Use the existing layout when it is clear. Create topic pages only when they have supported content. A small domain can combine related topics under separate headings. Split large pages by domain concept or workflow, then update the index and links.

| Page | Content |
| --- | --- |
| `index.md` | Domain identity, provisional or confirmed scope, exclusions and neighbours, mental model, reading order, coverage table, gaps, and continuation point |
| `concepts.md` | Domain glossary, actors, entities, responsibilities, rules, and reasons |
| `system-map.md` | Responsibilities across services, repositories, teams, data stores, external systems, and owners; unexplored boundaries |
| `workflows.md` | End-to-end business operations across systems, contracts, handoffs, and failure handling |
| `current-state.md` | Legacy and deployed new behaviour, workflows, integrations, and operational scope |
| `target-state.md` | Proposed or approved direction, rationale, implementation progress, and transition conditions |
| `edge-cases.md` | Supported failure and boundary cases, differences between systems, and migration effects |
| `sources.md` | Stable source IDs, exact locators, dates or revisions, review dates, scope, and access limitations |
| `open-questions.md` | Unresolved contradictions and gaps; these entries are not established domain knowledge |

Keep discovery metadata in the global `~/.domains/index.md` catalogue. See [memory lifecycle](../../domain-work/references/memory-lifecycle.md) for its format and pending entries, and [read memory](../../domain-work/references/read-memory.md) for discovery and freshness. The catalogue is not another copy of domain facts.

## Claims and citations

Write a factual statement with its scope and a nearby link to the source register entry. Several sentences may share a citation only if the source supports them all. Separate a supported statement from an inference or an unresolved part.

Use stable IDs such as S1. Give each register entry a heading such as `## S1` so links like `[S1](sources.md#s1)` resolve. When moving a page, update relative paths. Cite a code symbol and revision, document section and version, Slack message or thread, incident section, or a precise local excerpt. An entire repository or search-result page is not a precise locator.

Each source entry records:

- Exact URL or local file locator and relevant section, line, message, or symbol.
- Author or owning function when available, and source type.
- Source date and revision when available; review date.
- Relevant environment, cohort, region, and time scope.
- What was reviewed, what it supports, and any access or evidence limits.
- Pages or sections using the source, when known, to support targeted drift checks.

An excerpt can support a claim about its contents without proving the underlying system behaves that way. Mark a missing original as not reviewed. Record blocked searches separately from reviewed sources. Never fabricate a URL, revision, date, or unavailable content.

Source repositories can live anywhere. Keep their locators usable from the global knowledge base: use known repository URLs with revisions and precise locations, or explicit local paths with revisions. A relative path that worked inside a service repository may not resolve from `~/.domains/`.

## Status

Current state means behaviour supported for a stated operational scope. Target state means intended behaviour and must identify whether it is proposed, approved, or in progress. A partial rollout can appear in both pages with different scopes.

Use an explicit `As of` date and evidence scope for time-sensitive sections. A review date is not a new observation date. If evidence is historical, say so; do not silently describe it as today's state.

## Edge-case entry

Record: trigger or precondition; legacy behaviour; new behaviour; coexistence or migration effect; consequence; sources; and unknowns. Use `Unknown` for unsupported cells. State whether behaviour was observed, tested, configured, or intended.

## Open-question entry

Record the question, competing claims and their sources, affected scope, impact on decisions, and evidence needed to resolve it. Include an owner or contact only if known. Mark resolution with supporting evidence; preserve the original issue briefly. Do not choose a side by seniority, majority vote, recency alone, or a confidence score.

## Example: partial rollout

Suppose a supplied production configuration records EU v2 rollout at 10%, while a product announcement says everyone uses v2.

Current state: “The reviewed production configuration sets EU v2 rollout to 10%; it does not measure actual customer exposure.” Cite that configuration.

Open question: “Does the announcement refer to availability, eligibility, or actual rollout? Resolve its scope against deployment evidence.” Cite both sources.

Do not average the claims or call either source universally authoritative. Preserve the supported configuration fact while keeping the broader rollout claim unresolved.
