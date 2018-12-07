"""
( 2 )  x >  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 2
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 2 = 14.12
Came to:
2.00x >  14.12
Result:
x < 7.06
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 2")
# -------------------------------------------------
