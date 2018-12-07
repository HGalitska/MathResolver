"""
( 2 )  x >  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 4
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 4 = 23.52
Came to:
2.00x >  23.52
Result:
x < 11.76
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 4")
# -------------------------------------------------
