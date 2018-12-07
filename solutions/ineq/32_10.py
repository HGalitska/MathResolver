"""
( 2 )  x >  ( 3 )  / ( 1 )  * 20
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( 1 )  * 20 = 60.00
Came to:
2.00x >  60.00
Result:
x < 30.0
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( 1 )  * 20")
# -------------------------------------------------
