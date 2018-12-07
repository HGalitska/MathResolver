"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 31
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 31 = 109.43
Came to:
2.00x >  109.43
Result:
x < 54.715
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 31")
# -------------------------------------------------
