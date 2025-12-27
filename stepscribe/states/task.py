from dataclasses import dataclass, field
from typing import Any

from ..components import Catcher, Retry
from .base_state import State, empty_dict, empty_list


@dataclass
class Task(State):
    resource: str = ""
    arguments: dict = field(default_factory=empty_dict)
    assign: Any = ""
    credentials: str | None = None
    retry: list[Retry] = field(default_factory=empty_list)
    catch: list[Catcher] = field(default_factory=empty_list)
    timeout_seconds: int = 999999
    heartbeat_seconds: int = 999999

    def __post_init__(self) -> None:
        self.type_ = "Task"
        return
