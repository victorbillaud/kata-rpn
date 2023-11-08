str = "20 2 +"


def rpn_reader(expression: str) -> int:
    items = expression.split(" ")

    stack = []

    for item in items:
        if item == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(b + a)
        elif item == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b - a)
        else:
            stack.append(int(item))

    return stack.pop()
