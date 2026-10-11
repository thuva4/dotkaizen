"""Synthetic Orders scheduling excerpt. Provider behaviour is not included."""

RETRY_DELAY_SECONDS = 1200


def retry_request(order_id, original_key):
    return {"order_id": order_id, "idempotency_key": original_key}
