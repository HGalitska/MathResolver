"""
( 4 + 3 + floor ( 6.4 ) ) 

Compute individual results:
4.0 + 3.0 => 7.0
7.0 + 6.4 => 13.4
Result: 13.40
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("( 4 + 3 + floor ( 6.4 ) ) ")