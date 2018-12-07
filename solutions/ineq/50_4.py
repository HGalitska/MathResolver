"""
( 2 )  x >  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 3
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 3 = 17.64
Came to:
2.00x >  17.64
Result:
x < 8.82
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 3")
# -------------------------------------------------
