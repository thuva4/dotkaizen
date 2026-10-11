# Domain knowledge skills

Four small skills for building domain understanding from scattered evidence. The skills create and maintain ordinary Markdown files. They cover legacy behaviour, intended changes, edge cases, and learning.

| Skill | Use it to |
| --- | --- |
| [domain-work](../skills/domain-work/SKILL.md) | Answer domain questions or use domain memory during project work |
| [domain-build](../skills/domain-build/SKILL.md) | Build a domain map from available source material |
| [domain-update](../skills/domain-update/SKILL.md) | Maintain an existing knowledge base as evidence changes |
| [domain-learn](../skills/domain-learn/SKILL.md) | Learn the domain through explanations, scenarios, and feedback |

## Use

The domain defines the knowledge boundary. A domain can span multiple services, repositories, teams, and external systems.

The skills store one canonical knowledge base per domain at `~/.domains/<domain-slug>/`, shared across all projects. They expand `~` to your home directory and reuse existing domain directories. Give the agent the domain, relevant repositories, and source scope. Project documentation provides a local view and links to the canonical domain explanation rather than copying it.

The skill definitions stay in this repository. Domain information and saved learning notes go under `~/.domains/`. You do not need to provide a storage path on each request.

For ordinary project work, start with:

```text
Use $domain-work while I investigate this refund design.
Find the relevant domain across services, check decision-relevant evidence,
then reconcile supported discoveries before finishing.
```

Work mode authorizes supported note maintenance for the task. Read-only requests still take precedence. In Claude Code use `/domain-work`. On first write, the skill creates the catalogue and a local Git repository under `~/.domains/`, with snapshots and no remote.

For a direct answer, use:

```text
Use $domain-work in direct recall mode.
Why did we choose this refund retry window, and what does the evidence
say about legacy versus new behaviour? Cite sources and identify gaps.
```

Question-only requests select direct recall automatically. Recall reads relevant evidence and answers without a quiz or memory writes. New evidence can correct the answer without silently changing saved notes. To persist a correction, explicitly request an update. In Claude Code, use `/domain-work` followed by the same question.

Direct recall loads the short [reader procedure](../skills/domain-work/references/read-memory.md) and [answer contract](../skills/domain-work/references/direct-recall.md). The reader preserves consistent snapshots, scoped discovery, and freshness checks. Write and recovery instructions load when a task authorizes memory changes.

Other requests after installing the skills:

```text
Use $domain-build to map refunds into ~/.domains/refunds.
Trace the full workflow across orders, payments, the provider, ledger,
and reporting. These are starting points; identify other relevant systems.
Use supplied ADRs, incidents, code, deployment records, and available
source systems. Cover legacy behaviour, new components, and coexistence.
Record missing access and unexplored dependencies.
```

```text
Use $domain-update on ~/.domains/refunds with this
rollout record and the implementation evidence from this service.
Assess effects on the full workflow, upstream and downstream systems,
contracts, migration, and edge cases. Keep local findings scoped;
do not infer global deployment from a change in one service.
```

```text
Use $domain-learn with ~/.domains/refunds.
Teach me the end-to-end refund workflow and this service's responsibilities.
Compare legacy and new timeout and retry behaviour.
Ask one scenario question at a time and check my reasoning.
```

Without installing, ask the agent to read the relevant `skills/<name>/SKILL.md` in this repository and apply it. Keep the four sibling directories available. In Claude Code, installed skills use `/domain-work`, `/domain-build`, `/domain-update`, and `/domain-learn`.

## During everyday work

Use `domain-work` as the task wrapper for shared domain memory during project work. Normal exploration, design, and coding continue as usual; the skills manage and teach the domain knowledge around that work.

| Activity | How to use the knowledge base |
| --- | --- |
| Start or explore a domain | Use `domain-build` to map domain concepts, system boundaries, and end-to-end workflows from accessible evidence |
| Ask a factual or historical question | Use domain-work direct recall for a cited answer with dates, scope, and unknowns; no writes or quiz |
| Investigate a service | Read the domain index and relevant workflow; compare the local implementation with its documented responsibilities |
| Design a change | Assess affected business rules, contracts, upstream and downstream systems, coexistence, migration, and edge cases; keep assumptions visible |
| Record a design decision | Use `domain-update` to record proposed or approved intent separately from current behaviour |
| Finish implementation | Use `domain-update` to record supported implementation and test results; deployment remains unknown without deployment evidence |
| Receive new evidence | Update affected domain explanations, source records, summaries, and open questions |
| Prepare for a discussion or review | Use `domain-learn` for a workflow explanation, stakeholder perspectives, and scenario questions |

For a coding or exploration task, a useful starting request is:

```text
Use $domain-work. Find the refunds domain through ~/.domains/index.md.
Read the selected domain index and relevant pages.
Locate this service's responsibilities in the end-to-end workflow.
Investigate the change here, then assess effects on upstream systems,
downstream systems, contracts, and migration behaviour.
Separate evidence from assumptions. Identify systems you could not inspect.
```

Update the canonical knowledge base when evidence changes, behaviour changes, or a question is resolved. An update is not required for every task. A local finding retains its service, revision, environment, cohort, and time scope; it does not establish the behaviour of the whole domain.

## Use with agent roles

Domain knowledge work is separate from task execution by the [agent roles](../README.md#roles). The orchestrator, explore, and tester do not access `~/.domains/`. domain-reader answers one bounded question for the orchestrator with a short cited brief, and judge reads memory to verify changes. Both use direct recall without writes. Record lesson candidates about these skills in `tests/failures.local.md` (gitignored; template in [tests/failures.md](../tests/failures.md)).

## Install and activate

These steps are for local Codex, Claude Code, and opencode sessions on the computer that holds `~/.domains/`. Remote or cloud sessions need their own available skills and knowledge files. This repository does not install skills, edit global instructions, or change hooks automatically.

### 1. Install the skills

Use `~/.agents/skills/` for a new Codex installation, as documented in the [Codex skills guide](https://learn.chatgpt.com/docs/build-skills). Claude Code uses `~/.claude/skills/`, as documented in its [skills guide](https://code.claude.com/docs/en/skills). If an older Codex setup already discovers copies under `~/.codex/skills/`, check those before adding another copy. Keep one active copy of each skill per runtime.

opencode discovers skills from `~/.config/opencode/skills/`, `~/.claude/skills/`, and `~/.agents/skills/`, as documented in its [skills guide](https://opencode.ai/docs/skills/). It scans all three; the install command skips skills already present in any of them, so each skill is listed once. Skill names already match their directory names, as opencode requires.

Install with `python3 build.py install <claude|codex|opencode>` from the repository root, as described in the [README](../README.md#install). It copies all five skills, skips any skill already present in a directory the harness scans, and never overwrites local edits.

Keep each `references/` directory with its `SKILL.md`. Install the domain skills together: build, update, and learn use domain-work's shared references. Existing copies are not refreshed. Compare them with the repo and preserve local edits when updating. The set has no custom runtime scripts, packages, or connector requirements. Memory writes require Git and a configured Git identity.

### 2. Add persistent instructions

Append the following section once to your existing instruction file. Preserve your other instructions.

- Codex, across projects: `~/.codex/AGENTS.md`, or `AGENTS.md` under your configured `CODEX_HOME`. If `AGENTS.override.md` is active there, edit that active file instead; Codex uses it instead of `AGENTS.md`. For one repository, use its root `AGENTS.md`. See [Codex instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
- Claude Code, across projects: `~/.claude/CLAUDE.md`. For one repository, use its `CLAUDE.md`. See [Claude Code memory](https://code.claude.com/docs/en/memory).
- opencode, across projects: `~/.config/opencode/AGENTS.md`. It reads `~/.claude/CLAUDE.md` only when that file is absent. For one repository, use its root `AGENTS.md`. See [opencode rules](https://opencode.ai/docs/rules/).

```markdown
## Domain memory

Use domain-work only for business-domain questions or when I explicitly
ask for domain-memory work. Read its SKILL.md before use.
Follow its consistent-reader rules before accessing ~/.domains/.
Find domains through ~/.domains/index.md and verify their business scopes.

For question-only requests, use direct recall: answer with citations,
dates, scope, and material unknowns. Do not quiz or write memory.
For project work, retrieve relevant memory first and reconcile supported
discoveries at meaningful milestones and before finishing. Follow the
shared lock, recovery, and snapshot rules for any memory writes.
Explicit read-only requests take precedence. Save learning progress only
when requested. Do not apply domain memory to unrelated tasks.
```

The instruction chooses when the skill applies. The skill holds the detailed procedure. Do not paste the whole knowledge base into the instruction file. Repository instructions can alter runtime behaviour; verify activation inside each pilot repository.

### 3. Verify activation in a fresh session

Open a new session in a real project. Ask:

```text
List the instruction files and domain skills you loaded.
Explain when you would use domain-work direct recall versus work mode.
Do not create or modify any files.
```

Codex should expose `$domain-work`, `$domain-build`, `$domain-update`, and `$domain-learn`. Claude Code should expose the matching `/domain-work`, `/domain-build`, `/domain-update`, and `/domain-learn` commands. opencode lists them in its `skill` tool; ask the agent to load `domain-work` by name. In Claude Code, `/context` checks which instruction files loaded; `/memory` lists their locations for inspection or editing. If a skill is absent, check the installation directory, duplicate names, and active overrides, then restart the session. See [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude Code skills](https://code.claude.com/docs/en/skills), and [Claude Code memory](https://code.claude.com/docs/en/memory).

Then ask one known question about an existing domain. Check that the answer cites the correct source and scope, preserves unknowns, and leaves files unchanged. An explanation of the modes is a setup check; this actual question checks behaviour. If no domain exists yet, use domain-build with your pilot scope and sources first. A recall question must not create an empty knowledge base.

### Hooks

No hook is required for this setup. Persistent instructions select the skill, and explicit invocation remains available. This is a workflow instruction, not a guarantee that every model turn follows it.

For the pilot, use the setup above first. If sessions repeatedly miss activation after startup or compaction, an optional Claude Code `SessionStart` reminder can supply context at those events. It would remind the agent to apply the mode rules; it would not verify evidence or perform reconciliation itself. Claude Code documents this event and its context output in the [hooks reference](https://code.claude.com/docs/en/hooks#sessionstart).

A reminder hook should not write domain files, force a commit, or run an unconditional Stop loop. Those actions need the task's evidence, selected mode, and shared storage protocol. No hook or settings change is supplied or installed in this revision. Preserve existing hooks if adding a reminder after the pilot shows a need.

## Define the domain with human input

Start with a business question and representative workflows. Identify their outcomes, actors, rules, start and end points, and handoffs. Code, service ownership, and team structures provide evidence about responsibilities; they do not automatically define domain boundaries.

The agent records a short `Domain scope` section in `index.md`: organisation or context, purpose, workflows, inclusions, exclusions, neighbours, aliases, and boundary questions. A new model remains provisional until its scope is supported or confirmed. Scope confirmation does not verify every fact or make coverage complete.

The agent compares that scope before reusing notes. Merchant payment refunds and customer compensation can share terminology while having different rules. Link overlapping domains and record the relationship rather than merging them by name.

Human input is needed when different answers would materially change the domain selected, the files edited, or the conclusion. Examples include including chargebacks in refunds, expanding into compensation, or resolving conflicting business ownership. The agent should present the evidence, alternatives, and one focused question. It can continue independent exploration within an explicit provisional scope. It does not need approval for every read or routine update, or for scope already supplied by the user.

A user can confirm what to investigate. An appropriate business or technical owner may still be needed to resolve a policy or ownership question that sources cannot establish. The agent does not contact stakeholders without authorization.

## Work within large codebases

Use a bounded investigation pass. Supply a workflow, question, source scope, and investigation limit where possible. Otherwise the agent starts with one representative workflow and a short named source set. It follows relevant handoffs rather than scanning every repository or loading every source record.

The index or system map records coverage by workflow: inspected systems and evidence, status, gaps, and next check. Status distinguishes reviewed, inconclusive, inaccessible, and uninspected areas. A pass stops when its question is supported, its stated limit is reached, or progress needs missing evidence or a consequential decision. It records a continuation point for the next session.

For maintenance, the agent searches changed source IDs and affected terms across the selected domain's summaries, workflows, contracts, and edge cases. It preserves historical evidence. Implications for uninspected systems and other domains remain follow-up work.

All memory writes use one global atomic directory lock, including catalogue, learning, and pending entries. Writers investigate first, then acquire the lock for a short update. They re-read, preserve raw recovery copies, check and commit the update, and release their owned lock. Readers use one committed snapshot during a write. Cooperating local agents get exclusion; editors that ignore the protocol can still interfere. See [storage and recovery](../skills/domain-work/references/storage-and-recovery.md).

The global directory shares knowledge across projects in your home directory. It does not create a shared enterprise service across users. The [Astra review](enterprise-review.md) describes the limits; controlled trials on real tasks are still needed before claiming enterprise reliability.

## Knowledge-base layout

The global directory can contain several domains:

```text
~/.domains/
  index.md              # Catalogue: context, aliases, outcomes, services, links
  .git/                 # Local version history, created on first write
  .gitignore            # Excludes temporary lock and recovery copies
  .recovery/            # Raw pre-edit Markdown copies, excluded from facts
  refunds/
    index.md
    concepts.md
    system-map.md
    workflows.md
    current-state.md
    target-state.md
    edge-cases.md
    sources.md
    open-questions.md
    pending.md           # Only for unfinished discoveries / continuation
    learning.md          # Only when saving learning notes
  another-domain/
```

The build skill creates the selected domain directory as needed. Start with `index.md`, `sources.md`, and `open-questions.md`. Add supported topic pages as evidence becomes available. Combine or split topics to keep reading simple. See the [page format](../skills/domain-build/references/knowledge-base.md).

`system-map.md` connects domain responsibilities to services, repositories, data stores, external systems, and owners. `workflows.md` follows business operations across those boundaries, including contracts, handoffs, failure handling, and reconciliation where supported. Record unknown responsibilities and missing evidence as questions.

Choose domain names from business scope, not service or repository names. If several organisations have different domains with the same name, use distinct names such as `company-a-refunds` and `company-b-refunds`. Ask before merging ambiguous domains. Existing documentation elsewhere remains source material; the skills do not move or delete it automatically.

Use source locators that resolve from the global directory. Prefer precise repository URLs and revisions when known, or explicit local paths and revisions.

Assess coverage against domain workflows and system boundaries, not the number of repositories inspected. One thoroughly explored service can still leave most of a domain unexplored.

Established explanations contain scoped, supported claims. Unresolved claims stay on the questions page, which is clearly labelled as unresolved. The index exposes material gaps. Learning notes record personal progress separately from domain facts.

## Source handling

Use available source tools or supplied Markdown, documents, exports, and excerpts. Slack, Atlassian, GitHub, and other services are optional sources. If access is unavailable, the agent records that limitation and works from accessible evidence. These skills do not create connector access or publish changes to external systems.

Evidence is judged for the claim being made, not the author's seniority. Approved intent, merged implementation, configured rollout, and observed production behaviour remain distinct. No workflow guarantees perfect accuracy or complete coverage; citations and visible questions make the limits reviewable.

## Freshness, history, and recovery

At task start, the agent checks source revisions and scope for decision-relevant claims when change is reported or current behaviour matters. Inaccessible evidence stays dated and explicitly unverified for current decisions. It does not refresh a whole domain by changing a date. Rechecks happen during use; no background source monitor runs.

At milestones and task completion, the agent saves supported discoveries, separates unresolved questions, and checkpoints unfinished investigations when useful. `pending.md` is explicitly unverified. Repeated unchanged evidence requires no duplicate entry or commit.

For a context handoff, the [task-state format](../skills/domain-work/references/memory-lifecycle.md#task-handoff) preserves the goal, constraints, completed work, evidence revisions, actual verification, next action, and completion condition. Read-only tasks keep the handoff in conversation. Authorized work can attach it to a relevant pending entry under the normal writer protocol. Temporary task status stays separate from established domain facts.

Before edits, raw copies preserve affected existing content under `.recovery/<task-token>/`. These copies are excluded from Git and factual retrieval. After consistency checks, each coherent update gets a new Git commit. Raw or inconsistent edits never become the published reader snapshot merely for backup. To recover, ask the agent to inspect history, preview the selected version, preserve newer work, and restore only the requested files or sections. Recovery is another commit. Failed commits leave an explicit interruption and owned lock for recovery; other sessions must not write around it.

Local history does not protect against disk loss. Choose an external backup separately if needed. Access and retention policy review is outside this revision's scope, as requested.

## Checks

[Behaviour scenarios](../tests/domain/scenarios.md) cover conflicting evidence, partial rollout updates, and unknown failure behaviour. [Validation notes](../tests/domain/validation.md) record what was checked and the remaining limits.

The [comparison guide](../tests/domain/evaluation.md) connects these scenarios to a 12-case workflow evaluation pack. It defines fixed inputs, repeated runs, citation checks, and cost measurements. Structural checks and isolated examples do not establish broad accuracy or cost improvements.
