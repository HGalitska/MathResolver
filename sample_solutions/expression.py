"""This module evaluates mathematical expressions."""

operators = set('+-/*()  ')


def evaluate(expr: 'String expression') -> 'Result of expression':
    expr = list(x for x in expr.replace(' ', ''))

    operators_in_expr = []
    operands_in_expr = []

    operand_buffer = []
    for char in expr:
        if char in operators:
            operators_in_expr.append(char)

            operands_in_expr.append(''.join(operand_buffer))
            operand_buffer = []
        else:
            operand_buffer.append(char)

    operands_in_expr.append(''.join(operand_buffer))

    print("Operators: ", operators_in_expr)
    print("Operands: ", operands_in_expr)


# evaluate('3.2+7.5- 8*2/100+12-3')


class A:
    def __init__(self):
        self.one = 1


a = A()
print(a.one)
a.two = 2
print(a.two)
