from dataclasses import dataclass, field
from typing import Any

from .base_state import State, empty_list


@dataclass
class Pass(State):
    type_ = "Pass"
    assign: list[dict] = field(default_factory=empty_list)
    output: Any = None


@dataclass
class Wait(State):
    type_ = "Wait"
    seconds: int = 60
    timestamp: str | None = None
