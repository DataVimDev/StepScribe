from dataclasses import dataclass, field


@dataclass
class ItemProcessor:
    start_at: str
    states: list
    processor_config: dict = field(default_factory=dict)  # ={"Mode": "INLINE"})

    def __post_init__(self) -> None:
        if "Mode" not in self.processor_config.keys():
            self.processor_config["Mode"] = "INLINE"
        elif self.processor_config["Mode"] not in ["INLINE", "DISTRIBUTED"]:
            raise ValueError(
                "The processor config mode must be 'INLINE' or 'DISTRIBUTED'"
            )

        if self.processor_config["Mode"] == "DISTRIBUTED":
            if "ExecutionType" not in self.processor_config.keys():
                self.processor_config["ExecutionType"] = "STANDARD"

        return
