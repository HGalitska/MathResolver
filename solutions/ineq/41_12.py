"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 22
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 22 = 77.66
Came to:
2.00x >  77.66
Result:
x < 38.83
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 22")
# -------------------------------------------------
