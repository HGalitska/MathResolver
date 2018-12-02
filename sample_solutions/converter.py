from math import sqrt, ceil, floor, trunc
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
    '+': (2, lambda x, y: x + y),
    '-': (2, lambda a, b: a - b),
    '*': (3, lambda a, b: a * b),
    '/': (3, lambda a, b: a / b),
    '^': (5, lambda a, b: a ** b),
    '**': (5, lambda a, b: a ** b),
    '%': (3, lambda a, b: a % b),
    'mod': (4, lambda a, b: a % b),
    'sqrt': (4, sqrt),
    'ceil': (4, ceil),
    'floor': (4, floor),
    'trunc': (4, trunc),
    '(': (1, 0)
}


def infix_to_postfix(infix_expr):
    # precedence = dict()
    # precedence["^"] = 4
    # precedence["^"] = 4
    # precedence["*"] = 3
    # precedence["/"] = 3
    # precedence["+"] = 2
    # precedence["-"] = 2
    # precedence["("] = 1

    stack = Stack()
    postfix_list = list()
    token_list = infix_expr.split()
    print(token_list)

    for token in token_list:
        print(stack.items)
        if token in "0123456789":
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


print(infix_to_postfix("8 + mod ( 3 + 2 * 4 )"))
