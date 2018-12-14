import solutions.param_ineq as ineq
from algorithms.ineq import solve as solve_ineq
import module_manager as mm

SIGNS = [">", "<", ">=", "<="]


def get_operation(expression):
    operation = tuple()
    for char in expression:
        if char in SIGNS:
            sign_index = expression.index(char)
            operation = (char, sign_index)
    return operation


def list_to_expression(list):
    result = ""
    for element in list:
        result += str(element) + " "
    return result


def minus_to_negative(string_expression):
    result = ""
    i = 0
    while i != len(string_expression):
        if string_expression[i] == '-' and string_expression[i + 1] == ' ':
            result += '+ -'
            i += 2
        else:
            result += string_expression[i]
            i += 1

    return result


def inv(operation):
    if operation == '+': return '-'
    if operation == '-': return '+'
    if operation == '*': return '/'
    if operation == '/': return '*'


# ( expr_x) x ( operation ) ( expr_a ) a >==< ( expr ) : [min, max]
def solve(expression):
    module = mm.generate_module_name(ineq, expression)
    mm.add_new_module(ineq, module)
    module_path = mm.get_path(ineq, module)
    mm.open_doc_string(module_path, expression)

    operation = get_operation(expression)

    right_part = expression[operation[1] + 1:]
    interval = right_part[right_part.index(':') + 1:].split()
    min_int = int(interval[1])
    max_int = int(interval[3])
    right_expression = right_part[:right_part.index(':')]

    left_part = expression[:operation[1] - 1]
    expr_x = left_part[: left_part.index('x')]
    expr_a = left_part[left_part.index('x') + 4: left_part.index('a')]

    a_operation = left_part[left_part.index('x') + 2: left_part.index('x') + 3]

    result = ""
    hot_points = [min_int]
    for a in range(min_int + 1, max_int + 1):
        ineq_string = expr_x + " x " + operation[0] + " " + right_expression + " " + inv(
            a_operation) + " " + expr_a + " * " + str(a)
        new_result = solve_ineq(ineq_string, True)
        mm.add_to_doc(module_path, "\n" + ineq_string + " => " + str(new_result))
        if result != new_result:
            prev_a = hot_points[len(hot_points) - 1]
            mm.add_to_doc(module_path, '\nFor a > ' + str(prev_a) + " : " + new_result)
            result = new_result
            hot_points.append(a)

    mm.close_doc_string(module_path, ineq, expression)
    mm.print_doc(module_path)


if __name__ == "__main__":
    solve("( 2 ) x * ( 1 ) a > ( 3 ) : [ -1 , 4 ]")
