"""
( 2 )  x >  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 2
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 2 = 11.76
Came to:
2.00x >  11.76
Result:
x < 5.88
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 2")
# -------------------------------------------------
