"""
3 * x^2 + 3 * x - 3 = 0
-------------------------------------------------
1. Get coefficients:

a: 3.0
b: 3.0
c: -3.0
2. Compute discriminant:

d = b^2 - 4 * a * c = 3.0^2 - 4 * 3.0 * -3.0 = 9.0 - -36.0 = 45.00
4. Compute first root:

x1 = (-b - sqrt(d)) / (2 * a) = -1.62
5. Compute second root:

x2 = (-b + sqrt(d)) / (2 * a) = 0.62
"""
if __name__ == '__main__':
    from algorithms.quadr_eq import solve

    solve("3 * x^2 + 3 * x - 3 = 0")
# -------------------------------------------------
