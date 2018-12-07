"""
( 4 + 3 + floor ( 6.4 ) )

Compute individual results:
4.0 + 3.0 => 7.0
floor(6.4) => 6.0
7.0 + 6.0 => 13.0
Result: 13.00
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("( 4 + 3 + floor ( 6.4 ) )")
