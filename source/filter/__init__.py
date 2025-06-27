from .operators import FILTERS

def parse_filter_expression(expr: str):
    for operator, filterClass in FILTERS.items():
        if operator in expr:
            column, raw_value = expr.split(operator, 1)
            value = try_cast(raw_value)
            return filterClass(column, value)

    raise ValueError(f"Undefenited operator type: {expr}")


def try_cast(value: str):
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value
