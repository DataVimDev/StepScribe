import json
from functools import reduce
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

    def to_asl_json(self, indent: int = 4) -> str:
        no_states_json = self.model_dump_json(exclude_none=True, exclude="States")
        state_machine = json.loads(no_states_json)
        state_machine["States"] = reduce(
            lambda x, y: x | y, [s.to_asl() for s in self.States]
        )

        state_machine_asl_json = json.dumps(state_machine)
        return state_machine_asl_json
