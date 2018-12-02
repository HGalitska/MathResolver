from converter import evaluate_expression


def who_is(expr):
    if 'x^2' in expr:
        return 'square equation.'
    elif 'a' in expr:
        return 'inequality with parameter.'
    elif '>' in expr or '<' in expr or '>=' in expr or '<=' in expr:
        return 'inequality.'
    else:
        return 'expression with result.'


expression = input("Enter mathematical expression.\n"
                   "Put ' ' around every operation and operand.\n"
                   "You can use mathematical functions like 'sqrt ( 4 )'.\n"
                   "For inequalities with parameter use 'a' for parameter.\n"
                   "For square equations use syntax 'a * x^2 + b * x + c',"
                   "where a, b, c are actual numbers.\n")

print('Expression is ', who_is(expression))
evaluate_expression(expression)
