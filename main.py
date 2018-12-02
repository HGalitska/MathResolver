from converter import evaluate_expression


def who_is(expr):
    if 'x^2' in expr:
        return 'quadratic equation.', 4
    elif 'a' in expr:
        return 'inequality with parameter.', 3
    elif '>' in expr or '<' in expr or '>=' in expr or '<=' in expr:
        return 'inequality.', 2
    else:
        return 'expression with result.', 1


def check_availability():
    pass


def do_work():
    expression = input("Enter mathematical expression.\n"
                       "Put ' ' around every operation and operand.\n"
                       "You can use mathematical functions like 'sqrt ( 4 )'.\n"
                       "For inequalities with parameter use 'a' for parameter.\n"
                       "For quadratic equations use syntax 'a * x^2 + b * x + c = 0',"
                       "where a, b, c are actual numbers.\n")

    print('Expression is', who_is(expression)[0])
    evaluate_expression(expression)


do_work()
