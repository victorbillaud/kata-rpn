from app import rpn_reader


def test_sum():
    res = rpn_reader("20 3 +")
    assert res == 23
