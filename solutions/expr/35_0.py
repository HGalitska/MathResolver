"""
floor ( 3 ) + 23 - ( sqrt ( 25 ) ) 

floor(3.0) => 3.0
3.0 + 23.0 => 26.0
sqrt(25.0) => 5.0
26.0 - 5.0 => 21.0
result: 21.00
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("floor ( 3 ) + 23 - ( sqrt ( 25 ) ) ")
