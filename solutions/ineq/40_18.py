"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 6
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 6 = 21.18
Came to:
2.00x >  21.18
Result:
x < 10.59
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 6")
# -------------------------------------------------
