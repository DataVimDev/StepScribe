from dataclasses import dataclass
from .base_state import State
from ..components.choice_rules import ChoiceRule

@dataclass
class Choice(State):
    type: str = 'Choice'
    choices: list[ChoiceRule]
    default: str

