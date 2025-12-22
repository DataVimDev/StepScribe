from dataclasses import dataclass
from .base_state import State
from ..components import Retrier, Catcher
from typing import Any

@dataclass
class Task(State):
    type: str='Task'
    resource: str
    arguments: str
    output: Any
    parameters: str|list|dict
    credentials: str
    result_path: Any
    result_selector: Any
    retry: list[Retrier]
    catch: list[Catcher]
    timeout_seconds: int
    timeout_seconds_path: str
    heartbeat_seconds: int
    heartbeat_seconds_path: str

