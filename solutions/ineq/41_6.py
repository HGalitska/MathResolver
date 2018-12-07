"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 16
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 16 = 56.48
Came to:
2.00x >  56.48
Result:
x < 28.24
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 16")
# -------------------------------------------------
