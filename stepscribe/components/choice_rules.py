from dataclasses import dataclass


@dataclass
class ChoiceRule:
    condition: str
    next_: str
