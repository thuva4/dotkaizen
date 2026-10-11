# Read consistent, relevant domain evidence

Apply this procedure before catalogue discovery or any canonical memory read. All paths are under the expanded `~/.domains/` root. Reading does not authorize writes.

## Select a consistent version

Use only a root-local Git repository whose resolved top-level matches the knowledge root. An inherited parent repository is not a knowledge snapshot. Record the root-local HEAD, or its absence.

Check `.write-lock` before reading. If held, resolve HEAD once and read every needed memory file from that same commit with `git show <commit>:<relative-path>`. Discover paths from that commit too, using `git ls-tree`, so partial worktree entries cannot affect domain selection. Label the snapshot and its date. If there is no committed snapshot, defer dependent memory conclusions. Supplied external evidence can still support an answer.

Without a lock, capture HEAD before discovery and reading, then check the lock and HEAD afterward. If a writer started or HEAD changed, discard the mixed read and use one committed snapshot. If no local HEAD exists and no lock is held, read existing notes as unversioned, dated evidence. Do not call them a published snapshot. If Git cannot be checked, report that limit and defer conclusions requiring a consistent snapshot.

Exclude `.recovery/` and partial worktree claims from factual retrieval. A pending entry is unverified task information. Before any authorized write, load [storage and recovery](storage-and-recovery.md), acquire the lock, and re-read affected files.

## Retrieve only what the task needs

Search the catalogue by organisation, outcome, aliases, and service identifiers. Verify candidates against their own scope. The catalogue supports discovery, not factual claims. When the catalogue is missing, incomplete, or has broken links, inspect immediate non-hidden domain directories and their scope sections. Use the selected snapshot for this discovery. Do not scan all topic pages or merge domains because names or services overlap.

Read the selected index and relevant workflow, source entries, open questions, and pending entries. Use section-based reads for large pages. Stop when the question is supported or its source limit is reached. Keep missing access and uninspected branches explicit.

## Check decision-relevant freshness

Preserve each consequential claim's scope, evidence type, source revision, and observation date. Recheck the actual source section when change is reported, revisions differ, evidence conflicts, or the answer requires current deployment, configuration, policy, or contract behaviour. Titles and timestamps alone do not establish unchanged content.

Stable historical answers can use dated evidence. If current evidence is unavailable, retain the dated account and make current applicability unknown. A review date is not a new observation date. One checked source does not make a whole domain current. In recall mode, report corrections in conversation without updating notes or check dates.
