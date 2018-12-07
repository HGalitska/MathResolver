"""
( 3 + sqrt ( 9 ) )  x >  ( 5 + sqrt ( 25 ) )  - ( 4 + 3 + floor ( 6.4 ) )  * 13
Compute expression in left part:
( 3 + sqrt ( 9 ) )  x = 6.00x

Compute expression in right part:
  ( 5 + sqrt ( 25 ) )  - ( 4 + 3 + floor ( 6.4 ) )  * 13 = -159.00
Came to:
6.00x >  -159.00
Result:
x < -26.5
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 3 + sqrt ( 9 ) )  x >  ( 5 + sqrt ( 25 ) )  - ( 4 + 3 + floor ( 6.4 ) )  * 13")
