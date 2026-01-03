from dataclasses import dataclass


@dataclass
class Retry:
    error_equals: list[str]
    interval_seconds: int | None = None
    max_attempts: int | None = None
    max_delay_seconds: int | None = None
    jitter_strategy: str | None = None
    backoff_rate: int | float | None = None
