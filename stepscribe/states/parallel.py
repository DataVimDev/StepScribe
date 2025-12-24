from dataclasses import dataclass
from typing import Any

from ..components import Catcher, Retrier
from ..state_machine import StateMachine
from .base_state import State


@dataclass
class Parallel(State):
    branches: list[StateMachine]
    parameters: str
    arguments: str
    output: Any
    assign: Any
    result_path: Any
    result_selector: Any
    retry: Retrier
    catch_: list[Catcher]
