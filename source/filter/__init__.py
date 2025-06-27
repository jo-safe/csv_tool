from .operators import FILTERS

def parse_filter_expression(expr: str):
    for symbol, filterType in FILTERS.items():
        if symbol in expr:
            column, raw_value = expr.split(symbol, 1)
            value = try_cast(raw_value)
            return filterType(column, value)

    raise ValueError(f"Неизвестный оператор в выражении: {expr}")


def try_cast(value: str):
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value
