from dataclasses import dataclass

from ..components.choice_rules import ChoiceRule
from .base_state import State


@dataclass
class Choice(State):
    type: str = "Choice"
    choices: list[ChoiceRule]
    default: str
