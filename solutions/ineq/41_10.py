"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 20
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 20 = 70.60
Came to:
2.00x >  70.60
Result:
x < 35.3
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 20")
# -------------------------------------------------
