"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 32
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 32 = 112.96
Came to:
2.00x >  112.96
Result:
x < 56.48
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 32")
# -------------------------------------------------
