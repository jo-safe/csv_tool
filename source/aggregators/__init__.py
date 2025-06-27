from .math import AGGREGATORS
from .base import BaseAggregator

def parse_aggregator_expression(expr: str) -> BaseAggregator:
    try:
        column, aggrType = expr.split("=", 1)
        aggrCls = AGGREGATORS[aggrType]
    except:
        raise ValueError(f"Invalid expression format: {expr}")
    return aggrCls(column)