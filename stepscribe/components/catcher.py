from dataclasses import dataclass


@dataclass
class Catcher:
    error_equals: list[str]
    next_: str
    output: str | None = None
    assign: dict | None = None
