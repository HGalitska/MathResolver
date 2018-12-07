"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 23
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 23 = 81.19
Came to:
2.00x >  81.19
Result:
x < 40.595
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 23")
# -------------------------------------------------
