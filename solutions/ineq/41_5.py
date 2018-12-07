"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 15
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 15 = 52.95
Came to:
2.00x >  52.95
Result:
x < 26.475
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 15")
# -------------------------------------------------
