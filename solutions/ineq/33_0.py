"""
( sin ( 90 ) * 134 - 24 )  x <= 3
-------------------------------------------------
1. Compute expression in left part:
( sin ( 90 ) * 134 - 24 )  x = 95.26x

2. Compute expression in right part:
3 = 3.00
3. Came to:
95.26x <=  3.00
4. Result:
x >= 0.03149275666596683
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( sin ( 90 ) * 134 - 24 )  x <= 3")
# -------------------------------------------------
