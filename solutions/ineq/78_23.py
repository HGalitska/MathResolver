"""
( 3 + sqrt ( 9 ) )  x >  ( 5 + sqrt ( 25 ) )  - ( 4 + 3 + floor ( 6.4 ) )  * 0
-------------------------------------------------
Compute expression in left part:
( 3 + sqrt ( 9 ) )  x = 6.00x

Compute expression in right part:
  ( 5 + sqrt ( 25 ) )  - ( 4 + 3 + floor ( 6.4 ) )  * 0 = 10.00
Came to:
6.00x >  10.00
Result:
x < 1.6666666666666667
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 3 + sqrt ( 9 ) )  x >  ( 5 + sqrt ( 25 ) )  - ( 4 + 3 + floor ( 6.4 ) )  * 0")
-------------------------------------------------
