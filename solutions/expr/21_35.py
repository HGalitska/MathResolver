"""
 ( 5 + sqrt ( 25 ) ) 

Compute individual results:
sqrt(5.0) => 2.24
sqrt(25.0) => 5.0
2.24 + 5.0 => 7.24
Result: 7.24
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve(" ( 5 + sqrt ( 25 ) ) ")
