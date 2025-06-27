import pytest
from filter import parse_filter_expression as parse
from filter.operators import MoreThanFilter, EqualsFilter

def test_parse():
    """ Обработка аргумента, который должен быть обработан нормально (строка) """
    filter = parse("brand=apple")
    assert isinstance(filter, EqualsFilter)
    assert filter.column == "brand"
    assert filter.value == "apple"

def test_parse_numeric_value():
    """ Обработка аргумента, который должен быть обработан нормально (вещественное число) """
    filter = parse("price>15.5")
    assert isinstance(filter, MoreThanFilter)
    assert filter.column == "price"
    assert filter.value == 15.5

def test_parse_missing_value():
    """ Обработка аргумента с отсутствующим значением """
    with pytest.raises(ValueError):
        parse("rating<")

def test_parse_missing_column():
    """ Обработка аргумента с отсутствующим значением имени столбца """
    with pytest.raises(ValueError):
        parse("=5")

def test_parse_undefinited_operator():
    """ Обработка аргумента с отсутствующим или не валидным оператором """
    with pytest.raises(ValueError):
        parse("keyvalue")