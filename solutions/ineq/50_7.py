"""
( 2 )  x >  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 1
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 1 = 7.06
Came to:
2.00x >  7.06
Result:
x < 3.53
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 1")
# -------------------------------------------------
