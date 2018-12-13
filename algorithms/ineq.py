from algorithms import expr as expr
import solutions.ineq as ineq
import module_manager as mm

SIGNS = [">", "<"]


def get_operation(expression):
    operation = tuple()
    for i in range(len(expression)):
        char = expression[i]
        if char in SIGNS:
            sign_index = expression.index(char)
            if expression[i + 1] == "=":
                char = char + "="
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


def solve(expression, log=True):
    module = mm.generate_module_name(ineq, expression)
    mm.add_new_module(ineq, module)
    module_path = mm.get_path(ineq, module)
    mm.open_doc_string(module_path, expression)

    operation = get_operation(expression)

    left_part = expression[:operation[1] - 2]
    right_part = expression[operation[1] + 3:]

    left_result = expr.solve(left_part, log)
    right_result = expr.solve(right_part, log)
    mm.add_to_doc(module_path, "1. Compute expression in left part:\n")
    mm.add_to_doc(module_path, left_part + "x = " + format(left_result, '.2f') + "x\n")

    mm.add_to_doc(module_path, "\n2. Compute expression in right part:\n")
    print(right_result)
    mm.add_to_doc(module_path, right_part + " = " + format(right_result, '.2f') + '\n')

    mm.add_to_doc(module_path, "3. Came to:\n")
    mm.add_to_doc(module_path,
                  format(left_result, '.2f') + "x " + operation[0] + "  " + format(right_result, '.2f') + '\n')

    mm.add_to_doc(module_path, "4. Result:\n")
    if left_result == 0:
        if right_result == 0:
            mm.add_to_doc(module_path, 'x is any')
        else:
            mm.add_to_doc(module_path, 'has no roots')


    result = ""
    inv_oper = ''
    if operation[0] == '>':
        inv_oper = '<'
    elif operation[0] == '>=':
        inv_oper = '<='
    elif operation[0] == '<':
        inv_oper = '>'
    elif operation[0] == '<=':
        inv_oper = '>='
    else:
        mm.add_to_doc(module_path, "Operation undefined.")
        mm.close_doc_string(module_path, ineq, expression)
        mm.print_doc(module_path)
        return "Operation undefined."

    result = "x " + inv_oper + " " + str(right_result / left_result)
    mm.add_to_doc(module_path, result)
    mm.close_doc_string(module_path, ineq, expression)
    if log:
        mm.print_doc(module_path)

    return result
