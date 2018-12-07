"""
( 3 + sqrt ( 9 ) )

Compute individual results:
sqrt(9.0) => 3.0
3.0 + 3.0 => 6.0
Result: 6.00
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("( 3 + sqrt ( 9 ) )")
