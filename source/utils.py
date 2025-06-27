def try_cast(value: str):
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        if value == "":
            raise ValueError("Empty string")
        return value