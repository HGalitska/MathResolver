"""Module for solving mathematical expressions with result."""

import module_manager as mm
import solutions.expr as expr

import math


# stack class for reverse polish notation
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


# operators available for use in expressions
OPERATORS = {
    '+': [2, lambda x, y: x + y, 2],
    '-': [2, lambda a, b: a - b, 2],
    '*': [3, lambda a, b: a * b, 2],
    '/': [3, lambda a, b: a / b, 2],
    '^': [5, lambda a, b: a ** b, 2],
    '**': [5, lambda a, b: a ** b, 2],
    '%': [3, lambda a, b: a % b, 2],
    '(': [1, 0, 0],
    ')': [1, 0, 0]
}


# getting mathematical expressions from math module
MATH_FUNCTIONS = list(func for func in dir(math) if func[0] != '_')


# convert infix expression to postfix expression for RPN
def infix_to_postfix(infix_expr):
    stack = Stack()
    postfix_list = list()
    token_list = infix_expr.split()

    for token in token_list:

        if token in MATH_FUNCTIONS:
            if token == "fsum":
                print("We do not support functions with iterables.")
                return None
            exec("from math import " + token + " as func")
            if isinstance(eval("func"), float):
                postfix_list.append(eval("func"))
                continue

            exec("OPERATORS[token] = []")
            exec("OPERATORS[token].append(4)")
            exec("OPERATORS[token].append(func)")
            exec("OPERATORS[token].append(1)")

            if OPERATORS[token][2] != 1:
                print("Please use mathematical functions with exactly one argument.")
                return None

        if token not in OPERATORS:
            try:
                token = float(token)
            except ValueError:
                return None
            postfix_list.append(float(token))
        elif token == '(':
            stack.push(token)
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = stack.pop()
        else:
            while (not stack.is_empty()) and (OPERATORS[stack.peek()][0] >= OPERATORS[token][0]):
                postfix_list.append(stack.pop())
            stack.push(token)

    while not stack.is_empty():
        postfix_list.append(stack.pop())
    return " ".join(str(v) for v in postfix_list)


# evaluate postfix expression
def eval_postfix(postfix_expr, module_path):
    operand_stack = Stack()

    token_list = postfix_expr.split()

    mm.add_to_doc(module_path, "\n1. Compute individual results:")

    for token in token_list:
        if token not in OPERATORS:
            operand_stack.push(float(token))
        else:
            if OPERATORS[token][2] == 2:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = eval_simple_operation(token, operand1, operand2)
                mm.add_to_doc(module_path,
                              "\n" + str(operand1) + " " + str(token) + " " + str(operand2) + " => " + str(result))
                operand_stack.push(result)
            else:
                operand = operand_stack.pop()
                result = eval_simple_operation(token, operand)
                mm.add_to_doc(module_path, "\n" + str(token) + "(" + str(operand) + ") => " + str(result))
                operand_stack.push(result)

    return operand_stack.pop()


def eval_simple_operation(operation, *operands):
    if len(operands) == 1:
        return float(format(OPERATORS[operation][1](operands[0]), '.2f'))
    return float(format(OPERATORS[operation][1](operands[0], operands[1]), '.2f'))


def solve(expression, log=True):
    module = mm.generate_module_name(expr, expression)
    mm.add_new_module(expr, module)
    module_path = mm.get_path(expr, module)
    mm.open_doc_string(module_path, expression)

    postfix = infix_to_postfix(expression)

    if postfix is not None:
        result = eval_postfix(postfix, module_path)
        mm.add_to_doc(module_path, "\n2. Result: " + format(result, '.2f'))
        mm.close_doc_string(module_path, expr, expression)
        if log:
            mm.print_doc(module_path)
        return result
    # if there is an error in expression, delete solution module
    else:
        mm.delete_module(expr, module)
        print("Some error. Try again!")


if __name__ == "__main__":
    solve("( 4 + 3 + floor ( 6.4 ) )")
