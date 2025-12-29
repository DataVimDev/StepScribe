from dataclasses import dataclass, field
from typing import Any

from ..components import Catcher, Retry
from .base_state import State, empty_dict, empty_list


@dataclass
class Task(State):
    resource: str = ""
    arguments: dict = field(default_factory=empty_dict)
    credentials: str | None = None
    retry: list[Retry] | None = None # = field(default_factory=empty_list)
    catch: list[Catcher] | None = None # = field(default_factory=empty_list)
    timeout_seconds: int | None = None
    heartbeat_seconds: int | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        self.type_ = "Task"
        return
