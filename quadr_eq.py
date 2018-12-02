from math import sqrt, trunc, copysign
from numpy import roots


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
    abc = get_abc(expression)
    a = abc[0]
    b = abc[1]
    c = abc[2]
    print("a:", a, "b:", b, "c:", c)

    d = b ** 2 - 4 * a * c
    print("d = b^2 - 4 * a * c = "
          + str(b) + "^2 - 4 * " + str(a) + " * " + str(c) + " = "
          + str(b ** 2) + " - " + str(4 * a * c) + " =", format(d, '.2f'))

    sol1 = (-b - sqrt(d)) / (2 * a)
    sol2 = (-b + sqrt(d)) / (2 * a)

    print("x1 =", "(-b - sqrt(d)) / (2 * a) = ", format(sol1, '.2f'))
    print("x2 =", "(-b + sqrt(d)) / (2 * a) = ", format(sol2, '.2f'))

    print("---------------------------------")
    print(format(roots(abc)[0], '.2f'))
    print(format(roots(abc)[1], '.2f'))


solve("3.67 * x^2 + 40 * x + 12 = 0")
