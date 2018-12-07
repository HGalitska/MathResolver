"""
( 2 )  x >  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 0
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 0 = 0.00
Came to:
2.00x >  0.00
Result:
x < 0.0
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 0")
# -------------------------------------------------
