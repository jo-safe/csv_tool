from .base import BaseAggregator
from typing import Any

class AvgAggregator(BaseAggregator):
    """ Агрегатор нахождения среднего арифметического """
    identifier = "avg"

    @staticmethod
    def check_type(var: str) -> bool:
        try:
            sum([var, var]) / 2
            return True
        except:
            return False

    def calc(self) -> Any:
        return sum(self.values) / len(self.values)

class MaxAggregator(BaseAggregator):
    """ Агрегатор нахождения максимального значения """
    identifier = "max"

    @staticmethod
    def check_type(var: str) -> bool:
        try:
            max([var, var])
            return True
        except:
            return False

    def calc(self) -> Any:
        return max(self.values)

class MinAggregator(BaseAggregator):
    """ Агрегатор нахождения минимального значения """
    identifier = "min"

    @staticmethod
    def check_type(var: str) -> bool:
        try:
            min([var, var]) / 2
            return True
        except:
            return False

    def calc(self) -> Any:
        return min(self.values)
    
AGGREGATORS = { cls.identifier: cls for cls in BaseAggregator.__subclasses__()}