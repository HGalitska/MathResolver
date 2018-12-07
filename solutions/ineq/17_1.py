"""
( 2 + 35 ) x < 10
Compute expression in left part:
( 2 + 35 ) x = 37.00x

Compute expression in right part:
 10 = 10.00
Came to:
37.00x <  10.00
Result:
x > 0.2702702702702703
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 + 35 ) x < 10")
