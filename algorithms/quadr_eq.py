from math import sqrt, trunc, copysign
from numpy import roots

import module_manager as mm
import solutions.quadr_eq as quadratic_equations


# a * x^2 + b * x + c = 0
def get_abc(expression):
    print(expression)
    expression = expression.replace("+", "1")
    expression = expression.replace("-", "-1")
    expression = expression.split()
    expression = expression[:-2]

    b = copysign(float(expression[4]), float(expression[3]))
    c = copysign(float(expression[8]), float(expression[7]))

    return float(expression[0]), b, c


def solve(expression):
    module = mm.generate_module_name(quadratic_equations, expression)
    mm.add_new_module(quadratic_equations, module)
    module_path = mm.get_path(quadratic_equations, module)
    mm.open_doc_string(module_path, expression)

    abc = get_abc(expression)
    a = abc[0]
    b = abc[1]
    c = abc[2]

    mm.add_to_doc(module_path, "\na: " + str(a) + "b: " + str(b) + "c: " + str(c))

    d = b ** 2 - 4 * a * c
    mm.add_to_doc(module_path, "\nd = b^2 - 4 * a * c = "
                  + str(b) + "^2 - 4 * " + str(a) + " * " + str(c) + " = "
                  + str(b ** 2) + " - " + str(4 * a * c) + " = " + format(d, '.2f'))

    if d < 0:
        mm.add_to_doc(module_path, "\n!!! No roots.")
        mm.close_doc_string(module_path)
        mm.print_doc(module_path)
        return

    sol1 = (-b - sqrt(d)) / (2 * a)
    sol2 = (-b + sqrt(d)) / (2 * a)

    mm.add_to_doc(module_path, "\nx1 = " + "(-b - sqrt(d)) / (2 * a) = " + format(sol1, '.2f'))
    mm.add_to_doc(module_path, "\nx2 = " + "(-b + sqrt(d)) / (2 * a) = " + format(sol2, '.2f'))

    mm.add_to_doc(module_path, "\n---------------------------------")
    mm.add_to_doc(module_path, "\n" + format(roots(abc)[0], '.2f'))
    mm.add_to_doc(module_path, "\n" + format(roots(abc)[1], '.2f'))

    mm.close_doc_string(module_path)
    mm.print_doc(module_path)
