from math import sqrt, ceil, floor, trunc

OPERATORS = {
    '+': (2, lambda x, y: x + y),
    '-': (2, lambda a, b: a - b),
    '*': (2, lambda a, b: a * b),
    '/': (2, lambda a, b: a / b),
    '^': (2, lambda a, b: a ** b),
    '**': (2, lambda a, b: a ** b),
    '%': (2, lambda a, b: a % b),
    'mod': (2, lambda a, b: a % b),
    'sqrt': (1, sqrt),
    'ceil': (1, ceil),
    'floor': (1, floor),
    'trunc': (1, trunc)
}
