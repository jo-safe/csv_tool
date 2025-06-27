from .math import AGGREGATORS
from .base import AggregatorType

# TODO unite AGGREGATORS and AggregatorType
def parse_filter_expression(expr: str):
    try:
        for aggregatorType, aggregatorClass in AGGREGATORS.items():
            if expr.split("=", 1)[1] == aggregatorType:
                column, aggrType = expr.split("=", 1)
                return aggregatorClass(column, AggregatorType(list(AGGREGATORS.keys()).index(aggrType)))
    except:
        raise ValueError(f"Undefenited aggregator type: {expr}")