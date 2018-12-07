"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 12
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 12 = 42.36
Came to:
2.00x >  42.36
Result:
x < 21.18
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 12")
# -------------------------------------------------
