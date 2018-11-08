"""This module evaluates mathematical expressions."""

operators = set('+-/*')


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

    pass


# evaluate('3.2+7.5- 8*2/100+12-3')
print(eval('3.2+7.5- 8*2/100+12-3'))

# TODO: ASK без дужок і складних операторів, можна eval() ???
