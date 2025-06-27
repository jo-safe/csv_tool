from abc import ABC, abstractmethod
from typing import Any

class BaseFilter(ABC):
    def __init__(self, column: str, value: Any):
        self.column = column
        self.value = value

    @abstractmethod
    def apply(self, row: dict[str, Any]) -> bool:
        pass