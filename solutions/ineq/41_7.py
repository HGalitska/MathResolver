"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 17
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 17 = 60.01
Came to:
2.00x >  60.01
Result:
x < 30.005
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 17")
# -------------------------------------------------
