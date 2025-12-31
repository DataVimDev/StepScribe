from dataclasses import dataclass, field
from typing import Any


@dataclass
class ResultWriter:
    resource: str
    parameters: Any
    writer_config: dict = field(
        default_factory={
            "Transformation": "NONE",
            "OutputType": "JSON",
        }
    )
