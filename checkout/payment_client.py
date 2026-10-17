"""Client for the external payment gateway."""

import httpx

GATEWAY_URL = "https://payments.shopfast.example/api/v1/charges"
TIMEOUT_S = 30.0


def charge(amount_cents: int, customer_id: str, idempotency_key: str) -> dict:
    """Create a charge through the payment gateway."""
    response = httpx.post(
        GATEWAY_URL,
        json={"amount_cents": amount_cents, "customer_id": customer_id},
        headers={"Idempotency-Key": idempotency_key},
        timeout=TIMEOUT_S,
    )
    response.raise_for_status()
    return response.json()
