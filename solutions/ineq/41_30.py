"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 10
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 10 = 35.30
Came to:
2.00x >  35.30
Result:
x < 17.65
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 10")
# -------------------------------------------------
