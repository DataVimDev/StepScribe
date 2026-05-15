import json
from functools import reduce
from typing import Literal

from pydantic import BaseModel

from .state_models import (  # noqa: F401
    Choice,
    DistributedMap,
    Fail,
    Map,
    Parallel,
    Pass,
    State,
    Succeed,
    Task,
    Wait,
)


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

        state_machine_asl_json = json.dumps(state_machine, indent=indent)
        return state_machine_asl_json


def load_asl_json(asl_json: str, is_file: bool = False) -> StateMachine:
    if not is_file:
        asl_dict = json.loads(asl_json)
    else:
        with open(asl_json, "r") as file:
            asl_dict = json.load(file)

    asl_states_dict = asl_dict["States"]
    states_list = [{**value, "Name": key} for key, value in asl_states_dict.items()]

    states_model_list = [eval(state["Type"])(**state) for state in states_list]
    asl_dict["States"] = states_model_list
    return StateMachine(**asl_dict)
