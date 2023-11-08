import math


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
            try:
                stack.append(float(item))
            except ValueError:
                raise ValueError(f"Invalid operand: {item}")

    if len(stack) != 1:
        raise ValueError("Expected at least 2 operands but found 1")

    return stack.pop()


def _handle_sum(stack: list[float]) -> float:
    try:
        a = stack.pop()
        b = stack.pop()
    except IndexError:
        raise ValueError("Expected at least 2 operands, got 1")
    return b + a


def _handle_substract(stack: list[float]) -> float:
    try:
        a = stack.pop()
        b = stack.pop()
    except IndexError:
        raise ValueError("Expected at least 2 operands but found 1")
    return b - a


def _handle_sqrt(stack: list[float]) -> float:
    try:
        a = stack.pop()
    except IndexError:
        raise ValueError("Expected at least 1 operands but found 0")
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number")
    return math.sqrt(a)


def _handle_multiply(stack: list[float]) -> float:
    try:
        a = stack.pop()
        b = stack.pop()
    except IndexError:
        raise ValueError("Expected at least 2 operands but found 1")
    return b * a


def _handle_divide(stack: list[float]) -> float:
    try:
        a = stack.pop()
        b = stack.pop()
    except IndexError:
        raise ValueError("Expected at least 2 operands but found 1")
    if a == 0:
        raise ZeroDivisionError("Cannot divide by 0")
    return b / a


def _handle_max(stack: list[float]) -> float:
    try:
        max_val = max(stack)
        stack.clear()
        return max_val
    except IndexError:
        raise ValueError("Expected at least 2 operands but found 1")
