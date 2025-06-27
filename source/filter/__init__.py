from utils import try_cast

from .operators import FILTERS
from .base import BaseFilter

def parse_filter_expression(expr: str) -> BaseFilter:
    for operator, filterClass in FILTERS.items():
        if operator in expr:
            column, raw_value = expr.split(operator, 1)
            if not (column and raw_value):
                raise ValueError(f"Empty column or value ({expr})")
            value = try_cast(raw_value)
            return filterClass(column, value)

    raise ValueError(f"Undefinited operator type: {expr}")