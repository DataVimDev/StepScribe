from dataclasses import dataclass
from typing import Any

@dataclass
class State:
    type_: str
    query_language: str = 'JSONata'
    next_: str
    end_: bool
    comment: str
    assign: dict
    output: Any

    def post_init():
        pass


