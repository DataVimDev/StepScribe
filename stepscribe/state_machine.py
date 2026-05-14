from typing import Literal

from pydantic import BaseModel

from .state_models import State


class StateMachine(BaseModel):
    StartAt: str
    States: list[State]
    Comment: str | None = None
    QueryLanguage: Literal["JSONata", "JSONPath"] = "JSONata"
    TimeoutSecs: int | None = None
    Version: str | None = None
