"""
( 3 + sqrt ( 9 ) ) 

Compute individual results:
sqrt(3.0) => 1.73
sqrt(9.0) => 3.0
1.73 + 3.0 => 4.73
Result: 4.73
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("( 3 + sqrt ( 9 ) ) ")
