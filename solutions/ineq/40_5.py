"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 4
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 4 = 14.12
Came to:
2.00x >  14.12
Result:
x < 7.06
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 4")
# -------------------------------------------------
