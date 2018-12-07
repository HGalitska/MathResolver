"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 30
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 30 = 105.90
Came to:
2.00x >  105.90
Result:
x < 52.95
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 30")
# -------------------------------------------------
