"""
( 2 )  x >  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 9
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 9 = 63.54
Came to:
2.00x >  63.54
Result:
x < 31.77
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 9")
# -------------------------------------------------
