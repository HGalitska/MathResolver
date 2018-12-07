"""
( 2 )  x >  ( 3 )  - ( 1 )  * 4
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  - ( 1 )  * 4 = -1.00
Came to:
2.00x >  -1.00
Result:
x < -0.5
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  - ( 1 )  * 4")
-------------------------------------------------
