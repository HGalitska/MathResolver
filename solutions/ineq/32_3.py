"""
( 2 )  x >  ( 3 )  / ( 1 )  * 13
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( 1 )  * 13 = 39.00
Came to:
2.00x >  39.00
Result:
x < 19.5
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( 1 )  * 13")
# -------------------------------------------------
