from typing import Any

from pydantic import BaseModel, Field, model_validator
from typing_extensions import Self


class ChoiceRule(BaseModel):
    Condition: str
    Next: str


class ItemProcessor_(BaseModel):  # noqa: N801
    StartAt: str
    States: list
    ProcessorConfig: dict = Field(default_factory=dict)  # ={"Mode": "INLINE"})

    @model_validator(mode="after")
    def check_processor_mode(self) -> Self:
        if "Mode" not in self.ProcessorConfig.keys():
            self.ProcessorConfig["Mode"] = "INLINE"
        elif self.ProcessorConfig["Mode"] not in ["INLINE", "DISTRIBUTED"]:
            raise ValueError(
                "The ProcessorConfig Mode must be 'INLINE' or 'DISTRIBUTED'"
            )

        if self.ProcessorConfig["Mode"] == "DISTRIBUTED":
            if "ExecutionType" not in self.ProcessorConfig.keys():
                self.ProcessorConfig["ExecutionType"] = "STANDARD"

        return self


class ItemReader_(BaseModel):  # noqa: N801
    Resource: str
    Arguments: Any
    ReaderConfig: dict = Field(
        default_factory={"InputType": "JSON", "Transformation": "NONE"}
    )


class ResultWriter_(BaseModel):  # noqa: N801
    Resource: str
    Parameters: Any
    WriterConfig: dict = Field(
        default_factory={
            "Transformation": "NONE",
            "OutputType": "JSON",
        }
    )


class Retrier(BaseModel):
    ErrorEquals: list[str]
    IntervalSeconds: int | None = None
    MaxAttempts: int | None = None
    MaxDelaySeconds: int | None = None
    JitterStrategy: str | None = None
    BackoffRate: int | float | None = None


class Catcher(BaseModel):
    ErrorEquals: list[str]
    Next: str
    Output: Any | None = None
    Assign: Any | None = None
