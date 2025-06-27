import csv
from typing import Any

def read_csv(filepath: str) -> dict[str, Any]:
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            typed_row = {k: infer_type(v) for k, v in row.items()}
            rows.append(typed_row)
        return rows

def infer_type(value: str):
    try:
        if '.' in value:
            return float(value)
        else:
            return int(value)
    except ValueError:
        return value
