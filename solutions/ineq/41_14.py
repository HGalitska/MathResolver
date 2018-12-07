"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 24
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 24 = 84.72
Came to:
2.00x >  84.72
Result:
x < 42.36
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 24")
# -------------------------------------------------
