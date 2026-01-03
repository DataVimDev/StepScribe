from dataclasses import dataclass
from typing import Any

from .base_state import State


@dataclass
class Succeed(State):
    output: Any = None

    def __post_init__(self) -> None:
        super().__post_init__()
        self.type_ = "Succeed"
        return


@dataclass
class Fail(State):
    cause: Any = None
    error: Any = None

    def __post_init__(self) -> None:
        super().__post_init__()
        self.type_ = "Fail"
        return
