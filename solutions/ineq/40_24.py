"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 2
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 2 = 7.06
Came to:
2.00x >  7.06
Result:
x < 3.53
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 2")
# -------------------------------------------------
