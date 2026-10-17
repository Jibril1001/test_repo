"""Access-token issuance and validation for the auth service."""

import time

import jwt

TOKEN_TTL_SECONDS = 3600


def issue(subject: str, secret: str) -> str:
    """Issue a signed access token for a subject."""
    now = int(time.time())
    payload = {"sub": subject, "iat": now, "exp": now + TOKEN_TTL_SECONDS}
    return jwt.encode(payload, secret, algorithm="HS256")


def verify(token: str, secret: str) -> dict:
    """Validate a token and return its claims."""
    return jwt.decode(token, secret, algorithms=["HS256"])
