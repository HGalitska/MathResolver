"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 25
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 25 = 88.25
Came to:
2.00x >  88.25
Result:
x < 44.125
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 25")
# -------------------------------------------------
