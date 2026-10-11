# Baseline observations

Date: 2026-10-10.

An independent agent received the three synthetic requests before any of the new skills existed. It did not read the proposed skill instructions or write files. Its proposed content was reviewed against [the scenarios](scenarios.md).

## Build

The agent distinguished configured rollout, approved intent, merged implementation, and the observed incident. It resisted the request to remove important caveats.

Its proposed layout was only `current-state.md`, `target-state.md`, and `sources.md`. It placed “Unresolved claims” inside current state. It supplied no navigable index, separate questions page, or structured legacy/new/coexistence edge case. Source entries named the supplied records but lacked precise locators and review metadata.

The build skill adds the missing page responsibilities, source metadata, and edge-case structure while retaining the useful evidence distinctions.

## Update

The agent preserved historical rollout evidence and source IDs. It also imported the build scenario's narrower ADR description into the independent update scenario and changed the given target:

> “Previous KB text: \"All regions intended [S2]\".”

It called that text a correction even though the update task supplied an all-region target. It did not propose index or edge-case edits or demonstrate a repeated application.

The update skill explicitly keeps task evidence separate and checks affected summaries, scope, and repeated application. The execution fixture has its own ADR excerpt to make the scenario boundary unambiguous.

## Learn

The agent already handled the central uncertainty correctly. It identified unknown fallback behaviour, separated general concepts from facts, and declined to certify expertise after one lesson. It proposed waiting for quiz answers and recording progress separately.

The learning skill preserves those behaviours as a reusable workflow. The subsequent execution check tests real file handling and whether the learner is asked a question before receiving its answer.

## Limits

This is one baseline sample, with all three tasks presented together. It is evidence of these observed choices, not a statistical comparison of model performance. The execution checks run each skill independently and inspect actual files.
