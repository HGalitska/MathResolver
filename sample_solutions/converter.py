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


OPERATORS = {
    '+': [2, lambda x, y: x + y, 2],
    '-': [2, lambda a, b: a - b, 2],
    '*': [3, lambda a, b: a * b, 2],
    '/': [3, lambda a, b: a / b, 2],
    '^': [5, lambda a, b: a ** b, 2],
    '**': [5, lambda a, b: a ** b, 2],
    '%': [3, lambda a, b: a % b, 2],
    'sqrt': [4, 0, 1],
    'ceil': [4, 0, 1],
    'floor': [4, 0, 1],
    'trunc': [4, 0, 1],
    '(': [1, 0, 0],
    ')': [1, 0, 0],
    '>': [0, 0, 2],
    '<': [0, 0, 2],
    '>=': [0, 0, 2],
    '<=': [0, 0, 2]
}

MATH_FUNCTIONS = ['sqrt', 'ceil', 'floor', 'trunc']


def infix_to_postfix(infix_expr):
    stack = Stack()
    postfix_list = list()
    token_list = infix_expr.split()

    for token in token_list:
        if token in MATH_FUNCTIONS:
            import math
            OPERATORS[token][1] = getattr(math, token)

        if token not in OPERATORS:
            postfix_list.append(token)
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
    return " ".join(postfix_list)


def postfix_eval(postfix_expr):
    operand_stack = Stack()

    token_list = postfix_expr.split()

    for token in token_list:
        if token not in OPERATORS:
            operand_stack.push(float(token))
        else:
            if OPERATORS[token][2] == 2:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = evaluate(token, operand1, operand2)
                operand_stack.push(result)
            else:
                operand = operand_stack.pop()
                result = evaluate(token, operand)
                operand_stack.push(result)

    return operand_stack.pop()


def evaluate(operation, *operands):
    if len(operands) == 1:
        return OPERATORS[operation][1](operands[0])
    return OPERATORS[operation][1](operands[0], operands[1])


expression = "3 + 7 % 34 - trunc ( 6.3 ** 2 ) + sqrt ( 4 ) + 50"
postfix = infix_to_postfix(expression)
print("postfix:", postfix)
result = postfix_eval(postfix)
print("actual:", result)

print("------------------------------")
from math import sqrt, ceil, floor, trunc
print(result == eval(expression))
