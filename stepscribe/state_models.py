import json
from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self

from .component_models import (
    Catcher,
    ChoiceRule,
    ItemProcessor_,
    ItemReader_,
    ResultWriter_,
    Retrier,
)


class State(BaseModel):
    Name: str
    Next: str | None = None
    End: bool | None = None
    Comment: str | None = None
    Assign: dict | None = None
    Output: Any = None
    QueryLanguage: str = "JSONata"

    @model_validator(mode="after")
    def check_end_next(self) -> Self:
        if self.End and self.Next is not None:
            raise ValueError("State cannot be an End state with a defined Next state.")
        return self

    def to_asl(self) -> dict:
        """
        Returns the State model as an ASL compatible dictionary of the form
        `{<state_name>: {<rest of state model>}}`
        """
        model_json = self.model_dump_json(exclude_none=True)
        dict_from_json = json.loads(model_json)
        asl_dict = {
            dict_from_json["Name"]: {
                k: v for k, v in dict_from_json.items() if k != "Name"
            }
        }
        return asl_dict

    def to_asl_json(self, indent: int = 4) -> str:
        """
        Amazon States Language json needs to be of the form
            `{<state_name>: {<rest of pydantic state model>}}`
        This function leverages pydantics serialization to dump the model to json (excluding unused optional fields) and restructures that JSON to be ASL compatible.
        """
        asl_dict = self.to_asl()
        asl_json = json.dumps(asl_dict, indent=indent)
        return asl_json


class Pass(State):
    Type: str = Field(default="Pass", frozen=True)


class Wait(State):
    Type: str = Field(default="Wait", frozen=True)
    Seconds: int | str | None = None
    Timestamp: datetime | None = None

    @model_validator(mode="after")
    def check_wait(self) -> Self:
        if self.Seconds is not None and self.Timestamp is not None:
            raise ValueError("Wait states can't have Seconds and Timestamp set.")
        elif self.Seconds is None and self.Timestamp is None:
            raise ValueError(
                "Wait state requires one of Seconds or Timestamp to be set."
            )
        return self


class Fail(State):
    Cause: Any = None
    Error: Any = None
    Type: str = Field(default="Fail", frozen=True)


class Succeed(State):
    Type: str = Field(default="Succeed", frozen=True)
    Output: Any = None


class Choice(State):
    Choices: list[ChoiceRule] = Field(default_factory=[])
    Default: str | None = None
    Type: str = Field(default="Choice", frozen=True)


class Parallel(State):
    Type: str = Field(default="Parallel", frozen=True)
    Branches: list = Field(default_factory=[])
    Arguments: str | None = None
    Retry: Retrier | None = None
    Catch: list[Catcher] | None = None


class Task(State):
    Type: str = Field(default="Task", frozen=True)
    Resource: str = ""
    Arguments: dict = Field(default_factory=dict())
    Credentials: str | None = None
    Retry: list[Retrier] | None = None
    Catch: list[Catcher] | None = None
    Timeout_Seconds: int | None = None
    Heartbeat_Seconds: int | None = None


class Map(State):
    Type: str = Field(default="Map", frozen=True)
    ItemProcessor: ItemProcessor_ | None = None
    Items: list | str | None = None
    ItemSelector: dict | None = None
    MaxConcurrency: int | str | None = None
    Retry: Retrier | None = None
    Catch: list[Catcher] | None = None


class DistributedMap(State):
    Type: str = Field(default="Map", frozen=True)
    ItemProcessor: ItemProcessor_ | None = None
    ItemReader: ItemReader_ | None = None
    Items: list | None = None
    ItemBatcher: list | None = None
    MaxConcurrency: int | str | None = None
    ToleratedFailurePct: int | str | None = None
    ToleratedFailureCount: int | str | None = None
    Label: str | None = None
    ResultWriter: ResultWriter_ | None = None
    ResultSelector: dict | None = None
    Retry: Retrier | None = None
    Catch: list[Catcher] | None = None
