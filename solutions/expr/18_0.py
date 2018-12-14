"""
4 + inf + pi + tau
-------------------------------------------------

1. Compute individual results:
4.0 + inf => inf
inf + 3.141592653589793 => inf
inf + 6.283185307179586 => inf
2. Result: inf
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("4 + inf + pi + tau")
# -------------------------------------------------
