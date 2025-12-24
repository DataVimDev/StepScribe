from dataclasses import dataclass
from typing import Any

from ..components import Catcher, Retrier
from .base_state import State


@dataclass
class Task(State):
    type: str = "Task"
    resource: str
    arguments: dict
    output: Any
    parameters: str | list | dict
    credentials: str
    result_path: Any
    result_selector: Any
    retry: list[Retrier]
    catch: list[Catcher]
    timeout_seconds: int
    timeout_seconds_path: str
    heartbeat_seconds: int
    heartbeat_seconds_path: str
