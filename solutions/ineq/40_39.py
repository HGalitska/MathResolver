"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 7
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 7 = 24.71
Came to:
2.00x >  24.71
Result:
x < 12.355
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 7")
# -------------------------------------------------
