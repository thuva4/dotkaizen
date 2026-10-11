"""Synthetic pay-r3 implementation excerpt. No deployment is implied."""

RETRY_KEY_SECONDS = 300


def retained(created_at, now):
    """The key expires at the boundary, using seconds."""
    return now < created_at + RETRY_KEY_SECONDS
