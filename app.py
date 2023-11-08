import math

str = "20 2 +"


def rpn_reader(expression: str) -> int:
    items = expression.split(" ")

    stack = []

    operators = {
        "+": _handle_sum,
        "-": _handle_substract,
        "sqrt": _handle_sqrt,
        "*": _handle_multiply,
        "/": _handle_divide,
    }

    for item in items:
        if item in operators:
            stack.append(operators[item](stack))

        else:
            stack.append(int(item))

    return stack.pop()


def _handle_sum(stack: list[int]) -> int:
    try:
        a = stack.pop()
        b = stack.pop()

        return b + a
    except IndexError:
        raise ValueError("Invalid RPN expression")


def _handle_substract(stack: list[int]) -> int:
    try:
        a = stack.pop()
        b = stack.pop()

        return b - a
    except IndexError:
        raise ValueError("Invalid RPN expression")


def _handle_sqrt(stack: list[int]) -> int:
    try:
        a = stack.pop()

        return math.sqrt(a)
    except IndexError:
        raise ValueError("Invalid RPN expression")


def _handle_multiply(stack: list[int]) -> int:
    try:
        a = stack.pop()
        b = stack.pop()

        return b * a
    except IndexError:
        raise ValueError("Invalid RPN expression")


def _handle_divide(stack: list[int]) -> int:
    try:
        a = stack.pop()
        b = stack.pop()

        return b / a
    except IndexError:
        raise ValueError("Invalid RPN expression")
