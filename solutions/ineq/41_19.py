"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 29
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 29 = 102.37
Came to:
2.00x >  102.37
Result:
x < 51.185
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 29")
# -------------------------------------------------
