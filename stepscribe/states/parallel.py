from dataclasses import dataclass, field
from typing import Any

from ..components import Catcher, Retry
from ..state_machine import StateMachine
from .base_state import State, empty_list


@dataclass
class Parallel(State):
    branches: list[StateMachine] = field(default_factory=empty_list)
    parameters: str = ""
    arguments: str = ""
    output: Any = None
    assign: Any = None
    retry: Retry = None
    catch_: list[Catcher] = field(default_factory=empty_list)
