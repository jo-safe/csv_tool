import csv
from typing import Any

from utils import try_cast

def read_csv(filepath: str) -> list[dict[str, Any]]:
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            typed_row = {k: try_cast(v) for k, v in row.items()}
            rows.append(typed_row)
        return rows