from dataclasses import dataclass
from typing import Any

from .base_state import State

@dataclass
class Pass(State):
    type_ = 'Pass'
    assign: list[dict]
    output: Any

@dataclass
class Wait(State):
    type_ = 'Wait'
    seconds: int
    timestamp: str


