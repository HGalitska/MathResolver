"""
( 2 )  x >  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 6
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 6 = 42.36
Came to:
2.00x >  42.36
Result:
x < 21.18
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 6")
# -------------------------------------------------
