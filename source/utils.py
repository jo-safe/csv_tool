def try_cast(value: str):
    """ Функция преобразования str в int или float (при возможности)"""
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        if value == "":
            raise ValueError("Empty string")
        return value