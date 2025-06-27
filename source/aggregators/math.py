from .base import BaseAggregator
from typing import Any

class AvgAggregator(BaseAggregator):
    def calc(self) -> Any:
        return sum(self.values) / len(self.values)

class MaxAggregator(BaseAggregator):
    def calc(self) -> Any:
        return max(self.values)

class MinAggregator(BaseAggregator):
    def calc(self) -> Any:
        return min(self.values)
    
AGGREGATORS = {"avg" : AvgAggregator, 
               "max" : MaxAggregator, 
               "min" : MinAggregator}    