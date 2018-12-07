"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 34
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 34 = 120.02
Came to:
2.00x >  120.02
Result:
x < 60.01
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 34")
# -------------------------------------------------
