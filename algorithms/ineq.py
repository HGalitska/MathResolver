SIGNS = [">", "<", ">=", "<="]


def get_operation(expression):
    operation = tuple()
    for char in expression:
        if char in SIGNS:
            sign_index = expression.index(char)
            operation = (char, sign_index)
    return operation


def solve(expression):
    expression = expression.split()
    print(expression)

    operation = get_operation(expression)
    left_part = ''.join(expression[:operation[1]])
    right_part = ''.join(expression[operation[1] + 1:])

    print(left_part)
    print(right_part)


solve("-1x + 3 > 10 - 2x")
