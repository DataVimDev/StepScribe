from dataclasses import dataclass, field

from ..components.choice_rules import ChoiceRule
from .base_state import State, empty_list


@dataclass
class Choice(State):
    choices: list[ChoiceRule] = field(default_factory=empty_list)
    default: str | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        self.type = "Choice"
        return
