"""
( 2 )  x >  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 1
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 1 = 5.88
Came to:
2.00x >  5.88
Result:
x < 2.94
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 1")
# -------------------------------------------------
