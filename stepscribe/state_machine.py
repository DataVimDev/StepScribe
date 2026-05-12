import json
from dataclasses import asdict, dataclass, is_dataclass
from typing import Literal

from .states import *  # noqa F403


class MachineEncoder(json.JSONEncoder):
    def default(self, obj):
        if is_dataclass(obj):
            obj_dict = asdict(obj)
            clean_obj_dict = {}
            for k, v in obj_dict.items():
                if k == "states":
                    clean_obj_dict["States"] = {}
                    for s in v:
                        s_state = eval(s.get("type_"))(**s)
                        clean_obj_dict["States"].update(json.loads(s_state.to_json()))
                elif k.endswith("_") and v is not None:
                    clean_obj_dict[k[0:-1].title().replace("_", "")] = v
                elif v is not None:
                    clean_obj_dict[k.title().replace("_", "")] = v
            return clean_obj_dict
        return super().default(obj)


@dataclass
class StateMachine:
    start_at: str
    states: list
    comment: str | None = None
    query_language: Literal["JSONata", "JSONPath"] = "JSONata"
    timeout_secs: int | None = None
    version: str | None = None

    def to_json(self) -> str:
        return json.dumps(self, indent=4, cls=MachineEncoder)
