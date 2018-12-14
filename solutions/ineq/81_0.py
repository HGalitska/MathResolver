"""
( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * 0
-------------------------------------------------
1. Compute expression in left part:
( sin ( 90 ) * 134 - 24 )  x = 95.26x

2. Compute expression in right part:
 ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * 0 = 8.58
3. Came to:
95.26x <  8.58
4. Result:
x > 0.09006928406466512
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( sin ( 90 ) * 134 - 24 )  x < = ( sin ( 90 ) * sqrt ( 93 ) )  + ( 453 - 4 )  * 0")
# -------------------------------------------------
