from dataclasses import dataclass, field

from ..components import Catcher, Retry
from .base_state import State, empty_list


@dataclass
class Parallel(State):
    branches: list = field(default_factory=empty_list)
    arguments: str | None = None
    retry: Retry | None = None
    catch_: list[Catcher] | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        self.type_ = "Parallel"
        return
