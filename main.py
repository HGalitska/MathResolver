import module_manager, importlib


def who_is(expr):
    if 'x^2' in expr:
        return 'quadratic equation.', 'quadr_eq'
    elif 'a' in expr and ('>' in expr or '<' in expr or '>=' in expr or '<=' in expr):
        return 'inequality with parameter.', 'param_ineq'
    elif '>' in expr or '<' in expr or '>=' in expr or '<=' in expr:
        return 'inequality.', 'ineq'
    else:
        return 'expression with result.', 'expr'


def check_availability():
    pass


module = __name__


def do_work():
    expression = input("Enter mathematical expression.\n"
                       "Put ' ' around every operation and operand.\n"
                       "You can use mathematical functions like 'sqrt ( 4 )'.\n"
                       "For simple ineq use '( expr ) x > expr' syntax.\n"
                       "For ineq with parameter: "
                       "( expr_x) x ( operation ) ( expr_a ) a >==< ( expr ) : [min, max].\n"
                       "For quadratic equations use syntax 'a * x^2 + b * x + c = 0',"
                       "where a, b, c are actual numbers.\n\n"
                       "To read from file enter 'FILE'.\n\n")

    if expression == 'FILE':
        file = open('input.txt', 'r')
        expression = file.read()
        file.close()

    description = who_is(expression)[0]
    type_id = who_is(expression)[1]
    print('Expression is', description)

    exec("import algorithms." + type_id + " as algo_package")
    exec("import solutions." + type_id + " as solution_package")
    exec("solution = module_manager.find_solution(solution_package, expression)")
    exec("if solution is None: algo_package.solve(expression)")


do_work()
