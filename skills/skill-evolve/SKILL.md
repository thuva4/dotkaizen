---
name: skill-evolve
description: Use when asked to review recorded skill or agent failures and propose instruction changes with eval cases. Proposes only; never edits skills, agents, or tests.
---

# Propose instruction changes from recorded failures

Read `tests/failures.local.md` in the dotkaizen repository; it holds the entries and is gitignored. If it does not exist, read `tests/failures.md` and say it is only the template. Ask for the path if neither can be found. Read the files that entries name, relative to that repository root, and `tests/evaluation.md` for the existing cases. Do not edit any file. The user decides what to apply.

## Find patterns

Use entries with status `open`. Group them by the instruction that caused the behaviour, not by symptom. A pattern needs two or more entries, or one entry with a consequential failure such as data loss, a false claim of verification, or a memory write that was not authorized. List single minor entries as "watching" and propose nothing for them.

For each pattern, check whether the behaviour comes from the instruction text, from missing context in the task, or from the model. Propose instruction changes only for the first. Report the others with their evidence.

## Propose

For each pattern, give one proposal:

- Entries: the F-numbers it covers.
- Cause: the exact instruction, quoted with file and section, or the missing instruction.
- Edit: the smallest change that addresses it, as a before/after diff. Prefer replacing or deleting text over adding it; state the file's word count after the edit.
- Held-in case: a task, fixture needs, and acceptance criteria that fail on the current version and should pass after the edit. Base it on the recorded failure.
- Risk: held-out cases (W1–W6, D1–D6) or other rules the edit could affect.

Never propose changes to held-out cases, fixtures, or acceptance criteria to make a candidate pass. A case change is a separate proposal, labelled as such.

## Finish

Rank proposals by consequence and number of entries. Recommend at most three for the next comparison, one change per comparison. Return proposals in conversation. Do not mark entries as resolved; the user updates status after the comparison in `evaluation.md`.
