import math

str = "20 2 +"


def rpn_reader(expression: str) -> float:
    items = expression.split(" ")

    stack = []

    operators = {
        "+": _handle_sum,
        "-": _handle_substract,
        "sqrt": _handle_sqrt,
        "*": _handle_multiply,
        "/": _handle_divide,
        "max": _handle_max,
    }

    for item in items:
        if item in operators:
            stack.append(operators[item](stack))

        else:
            stack.append(float(item))

    return stack.pop()


def _handle_sum(stack: list[float]) -> float:
    if len(stack) < 2:
        raise ValueError("Expected at least 2 operands, got less")
    try:
        a = stack.pop()
        b = stack.pop()

        return b + a
    except IndexError:
        raise ValueError("Expected at least 2 operands, got 1", a)


def _handle_substract(stack: list[float]) -> float:
    if len(stack) < 2:
        raise ValueError("Expected at least 2 operands, got less")
    try:
        a = stack.pop()
        b = stack.pop()

        return b - a
    except IndexError:
        raise ValueError("Invalid RPN expression")


def _handle_sqrt(stack: list[float]) -> float:
    if len(stack) < 1:
        raise ValueError("Expected at least 1 operands, got less")
    try:
        a = stack.pop()

        return math.sqrt(a)
    except Exception as e:
        raise Exception("Invalid RPN expression", e)


def _handle_multiply(stack: list[float]) -> float:
    if len(stack) < 2:
        raise ValueError("Expected at least 2 operands, got less")
    try:
        a = stack.pop()
        b = stack.pop()

        return b * a
    except IndexError:
        raise ValueError("Invalid RPN expression")


def _handle_divide(stack: list[float]) -> float:
    if len(stack) < 2:
        raise ValueError("Expected at least 2 operands, got less")
    try:
        a = stack.pop()
        b = stack.pop()
        
        if a or b == 0:
            raise ValueError("Cannot divide by 0")

        return b / a
    except IndexError:
        raise ValueError("Invalid RPN expression")
    
def _handle_max(stack: list[float]) -> float:
    if len(stack) < 2:
        raise ValueError("Expected at least 2 operands, got less")
    try:
        a = stack.pop()
        b = stack.pop()

        return max(a,b)
    except IndexError:
        raise ValueError("Invalid RPN expression")
