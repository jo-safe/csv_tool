from abc import ABC, abstractmethod
from typing import Any

class BaseFilter(ABC):
    """ 
    Базовый класс фильтра. 

    Все дочерние классы должны иметь определенное свойство operator
    для однозначного определения типа фильтра в коде.
    """
    def __init__(self, column: str, value: Any):
        self.column = column
        self.value = value

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "operator"):
            raise NotImplementedError(f"Class {cls.__name__} must define 'operator' attribute")

    @abstractmethod
    def apply(self, row: dict[str, Any]) -> bool:
        pass