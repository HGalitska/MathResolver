"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 3
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 3 = 10.59
Came to:
2.00x >  10.59
Result:
x < 5.295
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 3")
# -------------------------------------------------
