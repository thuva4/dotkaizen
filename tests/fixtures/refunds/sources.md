# Synthetic source excerpts

These records are evaluation material. They do not describe a real service.

## S1: pay-r2 contract

Revision pay-r2, 2026-09-01. Retry keys remain available for 15 minutes. This is an implementation contract. Deployment and business rationale are not recorded.

## S2: pay-r3 contract

Revision pay-r3, 2026-10-01. Retry keys remain available for five minutes and expire at the boundary. See `payments.py`. This is an implementation contract. Deployment, business rationale, and provider behaviour are not recorded.

## S3: rollout configuration

Revision rollout-r7, 2026-09-15. EU v2 is configured at 10%; US v2 is configured at 0%. These percentages do not measure actual customer exposure. No later deployment evidence is supplied.

## S4: approved decision

ADR-7, approved 2026-08-20. Orders must reuse the original idempotency key for retries. The decision does not specify key retention or the reason for any retention window. See `orders.py` for the supplied implementation excerpt.

## S5: stakeholder note

Note dated 2026-09-16: “Everyone now uses v2.” No environment, cohort, or deployment evidence accompanies this assertion.
