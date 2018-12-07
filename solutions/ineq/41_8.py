"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 18
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 18 = 63.54
Came to:
2.00x >  63.54
Result:
x < 31.77
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 18")
# -------------------------------------------------
