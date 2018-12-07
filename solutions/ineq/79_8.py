"""
( 3 + sqrt ( 9 ) )  x >  ( 5 + sqrt ( 25 ) )  - ( 4 + 3 + floor ( 6.4 ) )  * 18
Compute expression in left part:
( 3 + sqrt ( 9 ) )  x = 6.00x

Compute expression in right part:
  ( 5 + sqrt ( 25 ) )  - ( 4 + 3 + floor ( 6.4 ) )  * 18 = -224.00
Came to:
6.00x >  -224.00
Result:
x < -37.333333333333336
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 3 + sqrt ( 9 ) )  x >  ( 5 + sqrt ( 25 ) )  - ( 4 + 3 + floor ( 6.4 ) )  * 18")
