"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 26
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 26 = 91.78
Came to:
2.00x >  91.78
Result:
x < 45.89
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 26")
# -------------------------------------------------
