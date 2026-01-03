from dataclasses import dataclass, field

from ..components import Catcher, ItemProcessor, ItemReader, ResultWriter, Retry
from .base_state import State


def empty_processor():
    return ItemProcessor(start_at="", states=[])


def empty_reader():
    return ItemReader(resource="", arguments="")


@dataclass
class DistributedMap(State):
    item_processor: ItemProcessor = field(default_factory=empty_processor)
    item_reader: ItemReader = field(default_factory=empty_reader)
    items: list | None = None
    item_batcher: list | None = None
    max_concurrency: int | str | None = None
    tolerated_failure_pct: int | str | None = None
    tolerated_failure_count: int | str | None = None
    label: str | None = None
    result_writer: ResultWriter | None = None
    result_selector: dict | None = None
    retry: Retry | None = None
    catch: list[Catcher] | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        self.type_ = "Map"
        return


@dataclass
class Map(State):
    item_processor: ItemProcessor = field(default_factory=empty_processor)
    items: list | str | None = None
    item_selector: dict | None = None
    max_concurrency: int | str | None = None
    retry: Retry | None = None
    catch: list[Catcher] | None = None

    def __post_init__(self) -> None:
        super().__post_init__()
        self.type_ = "Map"
        return
