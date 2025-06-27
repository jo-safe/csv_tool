import pytest
from aggregators import parse_aggregator_expression as parse
from aggregators.math import AvgAggregator

def test_parse():
    """ Обработка аргумента, который должен быть обработан нормально """
    aggr = parse("price=avg")
    assert aggr.column == "price"
    assert isinstance(aggr, AvgAggregator)

def test_parse_undefinited_aggr_type():
    """ Обработка аргумента с нераспознаваемым значением """
    with pytest.raises(ValueError):
        parse("price=something")

def test_parse_missing_aggrType():
    """ Обработка аргумента с отсутствующим значением типа аггрегатора """
    with pytest.raises(ValueError):
        parse("price=")

def test_parse_missing_column():
    """ Обработка аргумента с отсутствующим значением столбца """
    with pytest.raises(ValueError):
        parse("=avg")