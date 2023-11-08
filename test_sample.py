from app import rpn_reader


class TestUnit:
    def test_sum(self):
        res = rpn_reader("20 3 +")
        assert res == 23

    def test_substract(self):
        res = rpn_reader("4 2 -")
        assert res == 2

    def test_mult(self):
        res = rpn_reader("4 2 *")
        assert res == 8