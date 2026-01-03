from dataclasses import dataclass, field
from typing import Any


@dataclass
class ItemReader:
    resource: str
    arguments: Any
    reader_config: dict = field(
        default_factory=dict
    )  # ={'InputType': 'JSON', 'Transformation': 'NONE'})
