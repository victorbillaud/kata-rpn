import pytest

from app import rpn_reader


class TestUnit:
    def test_sum(self):
        res = rpn_reader("20 3 +")
        assert res == 23
        assert rpn_reader("0 0 +") == 0
        assert rpn_reader("5 0 +") == 5
        assert rpn_reader("0 5 +") == 5
        assert rpn_reader("-5 5 +") == 0
        assert rpn_reader("5 -5 +") == 0
        assert rpn_reader("-0 5 +") == 5
        assert rpn_reader("-5 -5 +") == -10

    def test_sum_with_one_operand(self):
        try:
            rpn_reader("20 +")
            assert False
        except Exception:
            assert True

    def test_substract(self):
        res = rpn_reader("4 2 -")
        assert res == 2
        assert rpn_reader("10 0 -") == 10
        assert rpn_reader("0 10 -") == -10
        assert rpn_reader("0 0 -") == 0
        assert rpn_reader("-10 0 -") == -10
        assert rpn_reader("-10 -10 -") == 0
        assert rpn_reader("10 -5 -") == 15

    def test_product(self):
        res = rpn_reader("4 2 *")
        assert res == 8
        assert rpn_reader("5 0 *") == 0
        assert rpn_reader("0 5 *") == 0
        assert rpn_reader("5 -1 *") == -5
        assert rpn_reader("-5 1 *") == -5
        assert rpn_reader("-5 -1 *") == 5

    def test_sum_float_value(self):
        res = rpn_reader("4.5 3.5 +")
        assert res == 8
        assert rpn_reader("0.5 0 +") == 0.5
        assert rpn_reader("0.5 -5 +") == -4.5
        assert rpn_reader("-0.5 -5 +") == -5.5

    def test_max_value(self):
        res = rpn_reader("2 3 max")
        assert res == 3
        assert rpn_reader("-0.5 -5 max") == -0.5
        assert rpn_reader("-15 15 max") == 15

    def test_multiple_operators(self):
        res = rpn_reader("2 3 max 4 +")
        assert res == 7

    def test_divide_by_0(self):
        with pytest.raises(ZeroDivisionError):
            rpn_reader("2 0 /")
