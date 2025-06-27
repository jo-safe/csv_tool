from abc import ABC, abstractmethod
from typing import Any

class BaseAggregator(ABC):
    """
    Базовый класс агрегатора. 

    Все дочерние классы должны иметь определенный аргумент identifier
    для однозначного определения типа агрегатора в коде.

    Также в дочерних классах должны быть переопределены методы
        - check_type(t: type) - проверка типа данных для работы с данным агрегатором
        - calc(self) - вычисление требуемого значения
    """
    def __init__(self, column: str):
        self.column = column
        self.values = []

        # Тип агрегируемых значений, автоопределяемый при первом добавлении элемента
        self.valueType = None

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "identifier"):
            raise NotImplementedError(f"Class {cls.__name__} must define 'identifier' attribute")

    def clear(self):
        self.values = []
        self.valueType = None

    def add(self, row: dict[str, Any]):
        try:
            if self.values == [] or self.valueType is None:
                if not self.__class__.check_type(row[self.column]):
                    raise ValueError(f"Unsupported type {type(row[self.column])} to use in {self.__class__}")
                self.valueType = type(row[self.column])
            if isinstance(row[self.column], self.valueType):
                self.values.append(row[self.column])
            else:
                raise TypeError(f"{self.valueType} expected, got {type(row[self.column])}")
        except KeyError as e:
            raise KeyError(f"Unexisting column \"{self.column}\"")

    @staticmethod
    @abstractmethod
    def check_type(var: Any) -> bool:
        pass

    @abstractmethod
    def calc(self) -> Any:
        pass