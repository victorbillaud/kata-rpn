from app import rpn_reader


class TestUnit:
    def test_sum(self):
        res = rpn_reader("20 3 +")
        assert res == 23
