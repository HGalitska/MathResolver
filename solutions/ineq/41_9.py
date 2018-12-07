"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 19
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 19 = 67.07
Came to:
2.00x >  67.07
Result:
x < 33.535
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 19")
# -------------------------------------------------
