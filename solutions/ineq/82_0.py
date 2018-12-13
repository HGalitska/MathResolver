"""
( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * -2
-------------------------------------------------
1. Compute expression in left part:
( sin ( 90 ) * 134 - 24 )  x = 95.26x

2. Compute expression in right part:
 ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * -2 = -889.42
3. Came to:
95.26x <  -889.42
4. Result:
x > -9.336762544614738
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * -2")
# -------------------------------------------------
