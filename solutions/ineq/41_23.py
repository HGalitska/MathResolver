"""
( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 33
-------------------------------------------------
Compute expression in left part:
( 2 )  x = 2.00x

Compute expression in right part:
  ( 3 )  / ( sin ( 45 ) )  * 33 = 116.49
Came to:
2.00x >  116.49
Result:
x < 58.245
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 2 )  x >  ( 3 )  / ( sin ( 45 ) )  * 33")
# -------------------------------------------------
