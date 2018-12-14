"""
( 3 - 234 ) x <= 254
-------------------------------------------------
1. Compute expression in left part:
( 3 - 234 ) x = -231.00x

2. Compute expression in right part:
254 = 254.00
3. Came to:
-231.00x <=  254.00
4. Result:
x >= -1.0995670995670996
"""
if __name__ == '__main__':
    from algorithms.ineq import solve

    solve("( 3 - 234 ) x <= 254")
# -------------------------------------------------
