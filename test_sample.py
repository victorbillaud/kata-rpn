from app import rpn_reader


class TestUnit:
    def test_sum(self):
        res = rpn_reader("20 3 +")
        assert res == 23

    def test_sum_with_one_operand(self):
        try:
            rpn_reader("20 +")
            assert False
        except Exception:
            assert True

    def test_substract(self):
        res = rpn_reader("4 2 -")
        assert res == 2

    def test_mult(self):
        res = rpn_reader("4 2 *")
        assert res == 8
        
    def test_sum_float_value(self):
        res = rpn_reader("4.5 3.5 +")
        assert res == 8
    
    def test_max_value(self):
        res = rpn_reader("2 3 max")
        assert res == 3
    
    def test_multiple_operators(self):
        res = rpn_reader("2 3 max 4 +")
        assert res == 7