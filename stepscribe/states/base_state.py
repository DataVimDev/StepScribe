import json
from dataclasses import asdict, dataclass, is_dataclass
from typing import Any


def empty_list() -> list:
    """Returns an empty list."""
    return []


def empty_dict() -> dict:
    """Returns an empty dictionary."""
    return {}


class StateEncoder(json.JSONEncoder):
    def default(self, obj):
        if is_dataclass(obj):
            obj_dict = asdict(obj)
            clean_obj_dict = {}
            for k, v in obj_dict.items():
                if k.endswith("_"):
                    clean_obj_dict[k[0:-1]] = v
                else:
                    clean_obj_dict[k] = v
            return clean_obj_dict
        return obj


@dataclass
class State:
    name: str
    type_: str | None = None  # usually set in __post_init__
    next_: str | None = None
    end_: bool = True
    comment: str = ""
    output: Any = None
    query_language: str = "JSONata"

    def to_json(self) -> str:
        return json.dumps(self, indent=4, cls=StateEncoder)
