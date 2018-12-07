"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 13
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 13 = 45.89
Came to:
2.00x >  45.89
Result:
x < 22.945
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 13")
# -------------------------------------------------
