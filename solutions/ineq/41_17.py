"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 27
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 27 = 95.31
Came to:
2.00x >  95.31
Result:
x < 47.655
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 27")
# -------------------------------------------------
