"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 11
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 11 = 38.83
Came to:
2.00x >  38.83
Result:
x < 19.415
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 11")
# -------------------------------------------------
