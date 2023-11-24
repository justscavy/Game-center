from dataclasses import dataclass


@dataclass
class Account:
    """User account."""

    id: int
    name: str
    password: str