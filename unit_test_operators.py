import unittest

#definition of the RPN expression to make sure it's valid
def valid_rpn(expression):
    my_stack = []
    operators = set(['+', '-', '*', '/'])   #the list of operators containing operations which we need to make sure are contained in the stack
    tokens = expression.split()             #the split function is going to divide every components of the expression into a list
                                            #we're going to check according to the divided expression if we can figure out an operator
    for token in tokens:
        if token not in operators:
            my_stack.append(token)     #append a token to the string variables
        else:
            if len(my_stack) < 2:      #length of the stack cannot be inferior to 2 else it is impossible to make an operation.
                return False
            my_stack.pop()
            my_stack.pop()
            my_stack.append(token)

    return len(my_stack) == 1

class TestRPNValid(unittest.TestCase):  #class that is going to explore the different unit tests that comes through our mind to make sure they're valid or invalid RPNs
    def test_valid_rpn(self):
        self.assertTrue(valid_rpn("4 1 / 9 2 / +"))
        self.assertTrue(valid_rpn("4 7 +"))
        self.assertTrue(valid_rpn("9 6 - 8 +"))
    
    def test_invalid_rpn(self):
        self.assertFalse(valid_rpn("9 2 - / 3 *"))
        self.assertFalse(valid_rpn("6 +"))
        self.assertFalse(valid_rpn("2 3 * /"))

if __name__ == '__main__':
    unittest.main()