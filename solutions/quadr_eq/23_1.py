"""
1 * x^2 - 0 * x + 3 = 0
Get coefficients:

a: 1.0
b: -0.0
c: 3.0Compute discriminant:

d = b^2 - 4 * a * c = -0.0^2 - 4 * 1.0 * 3.0 = 0.0 - 12.0 = -12.00
!!! No roots.
"""
if __name__ == '__main__':
    from algorithms.quadr_eq import solve

    solve("1 * x^2 - 0 * x + 3 = 0")
