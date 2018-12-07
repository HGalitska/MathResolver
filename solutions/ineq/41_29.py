"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 14
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 14 = 49.42
Came to:
2.00x >  49.42
Result:
x < 24.71
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 14")
# -------------------------------------------------