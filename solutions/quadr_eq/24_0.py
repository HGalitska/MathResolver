"""
9 * x^2 - 7 * x + 45 = 0
-------------------------------------------------
1. Get coefficients:

a: 9.0
b: -7.0
c: 45.0
2. Compute discriminant:

d = b^2 - 4 * a * c = -7.0^2 - 4 * 9.0 * 45.0 = 49.0 - 1620.0 = -1571.00
!!! No roots.
"""
if __name__ == '__main__':
    from algorithms.quadr_eq import solve

    solve("9 * x^2 - 7 * x + 45 = 0")
# -------------------------------------------------
