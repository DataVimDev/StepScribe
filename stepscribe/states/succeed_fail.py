from dataclasses import dataclass
from typing import Any

from .base_state import State

@dataclass
class Succeed(State):
    type_ = 'Succeed'
    output: Any


@dataclass
class Fail(State):
    type_ = 'Fail'
    cause: Any
    error: Any

