import pytest
from aggregators import parse_aggregator_expression as parse
from aggregators.math import AvgAggregator

def test_parse():
    aggr = parse("price=avg")
    assert aggr.column == "price"
    assert isinstance(aggr, AvgAggregator)

def test_parse_undefinited_aggr_type():
    with pytest.raises(ValueError):
        parse("price=something")

def test_parse_missing_column():
    with pytest.raises(ValueError):
        parse("price=")

def test_parse_missing_aggrType():
    with pytest.raises(ValueError):
        parse("=avg")