import pytest
from aggregators.math import AvgAggregator, MaxAggregator, MinAggregator

rows = [
    {"price": 10},
    {"price": 20},
    {"price": 30},
]

def test_avg():
    aggr = AvgAggregator("price")
    for row in rows:
        aggr.add(row)
    assert aggr.calc() == 20

def test_max():
    aggr = MaxAggregator("price")
    for row in rows:
        aggr.add(row)
    assert aggr.calc() == 30

def test_min():
    aggr = MinAggregator("price")
    for row in rows:
        aggr.add(row)
    assert aggr.calc() == 10

def test_add_incorrect_type():
    aggr = AvgAggregator("price")
    aggr.add({"price": 10})
    with pytest.raises(TypeError):
        aggr.add({"price": "nan"})