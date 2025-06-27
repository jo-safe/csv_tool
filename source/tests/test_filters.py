from filter.operators import MoreThanFilter, LessThanFilter, EqualsFilter

row = {"price": 500, "name": "iPhone"}

def test_more_than():
    """ Тестирование фильтра "больше чем" """
    f = MoreThanFilter("price", 400)
    assert f.apply(row)

def test_less_than():
    """ Тестирование фильтра "меньше чем" """
    f = LessThanFilter("price", 600)
    assert f.apply(row)

def test_equals():
    """ Тестирование фильтра "равно" """
    f = EqualsFilter("price", 500)
    assert f.apply(row)

def test_diff_types():
    """ Тестирование фильтра, примененного на значение неизвестного столбца """
    f = EqualsFilter("something", 50)
    assert not f.apply(row)