"""
( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * 1
-------------------------------------------------
1. Compute expression in left part:
( sin ( 90 ) * 134 - 24 )  x = 95.26x

2. Compute expression in right part:
 ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * 1 = 457.58
3. Came to:
95.26x <  457.58
4. Result:
x > 4.803485198404367
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * 1")
# -------------------------------------------------
