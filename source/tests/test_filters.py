from filter.operators import MoreThanFilter, LessThanFilter, EqualsFilter

row = {"price": 500, "name": "iPhone"}

def test_more_than():
    f = MoreThanFilter("price", 400)
    assert f.apply(row)

def test_less_than():
    f = LessThanFilter("price", 600)
    assert f.apply(row)

def test_equals():
    f = EqualsFilter("price", 500)
    assert f.apply(row)

def test_diff_types():
    f = EqualsFilter("something", 50)
    assert not f.apply(row)