from .base import BaseAggregator
from typing import Any

class AvgAggregator(BaseAggregator):
    identifier = "avg"
    def calc(self) -> Any:
        return sum(self.values) / len(self.values)

class MaxAggregator(BaseAggregator):
    identifier = "max"
    def calc(self) -> Any:
        return max(self.values)

class MinAggregator(BaseAggregator):
    identifier = "min"
    def calc(self) -> Any:
        return min(self.values)
    
AGGREGATORS = { cls.identifier: cls for cls in BaseAggregator.__subclasses__()}