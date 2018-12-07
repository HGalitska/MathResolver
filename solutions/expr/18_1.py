"""
( 3 + sqrt ( 9 ) )

Compute individual results:
sqrt(3.0) => 1.73
1.73 + 9.0 => 10.73
Result: 10.73
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("( 3 + sqrt ( 9 ) )")
