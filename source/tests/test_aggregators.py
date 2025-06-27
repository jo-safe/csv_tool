import pytest
from aggregators.math import AvgAggregator, MaxAggregator, MinAggregator

rows = [
    {"price": 10},
    {"price": 20},
    {"price": 30},
]

def test_avg():
    """ Тестирование аггрегатора нахождения среднего значения с валидными значениям на входе """
    aggr = AvgAggregator("price")
    for row in rows:
        aggr.add(row)
    assert aggr.calc() == 20

def test_max():
    """ Тестирование аггрегатора нахождения максимального значения с валидными значениям на входе """
    aggr = MaxAggregator("price")
    for row in rows:
        aggr.add(row)
    assert aggr.calc() == 30

def test_min():
    """ Тестирование аггрегатора нахождения минимального значения с валидными значениям на входе """
    aggr = MinAggregator("price")
    for row in rows:
        aggr.add(row)
    assert aggr.calc() == 10

def test_add_incorrect_type():
    """ Тестирование аггрегатора с добавлением не-числового значения """
    aggr = AvgAggregator("price")
    aggr.add({"price": 10})
    with pytest.raises(TypeError):
        aggr.add({"price": "nan"})