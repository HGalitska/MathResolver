"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 21
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 21 = 74.13
Came to:
2.00x >  74.13
Result:
x < 37.065
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 21")
# -------------------------------------------------
