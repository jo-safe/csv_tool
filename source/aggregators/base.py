from abc import ABC, abstractmethod
from typing import Any

class BaseAggregator(ABC):
    def __init__(self, column: str):
        self.column = column
        self.values = []

        self.valueType = None

    def clear(self):
        self.values = []

    def add(self, row: dict[str, Any]):
        if self.values == [] or self.valueType is None:
            self.valueType = type(row[self.column])
        if isinstance(row[self.column], self.valueType):
            self.values.append(row[self.column])
        else:
            raise TypeError(f"{self.valueType} expected, got {type(row[self.column])}")

    @abstractmethod
    def calc(self) -> Any:
        pass