"""Shared logging configuration."""

import logging


def configure(level: str = "INFO") -> None:
    """Configure root logging for every service."""
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
    )
