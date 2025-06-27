from utils import try_cast

def test_infer_type_int():
    assert try_cast("42") == 42

def test_infer_type_float():
    assert try_cast("3.14") == 3.14

def test_infer_type_str():
    assert try_cast("hello") == "hello"

def test_infer_type_compl_float():
    assert try_cast(" 005.680") == 5.68