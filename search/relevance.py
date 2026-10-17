"""Relevance scoring for the search service."""

WEIGHTS = {"title": 1.0, "body": 0.5, "freshness": 0.2}


def score(hit: dict) -> float:
    """Score a single search hit."""
    return (
        WEIGHTS["title"] * hit.get("title_match", 0.0)
        + WEIGHTS["body"] * hit.get("body_match", 0.0)
        + WEIGHTS["freshness"] * hit.get("freshness", 0.0)
    )
