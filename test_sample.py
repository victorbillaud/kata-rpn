from app import rpn_reader


def test_sum():
    res = rpn_reader("20 3 +")
    assert res == 23
    assert rpn_reader("1 5 +") == 6
    assert rpn_reader("9 sqrt") == 3
    assert rpn_reader("4 2 + 3 -") == 3
    assert rpn_reader("-10 10 +") == 0

test_sum()