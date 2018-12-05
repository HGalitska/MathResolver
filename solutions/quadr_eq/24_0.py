"""
3 * x^2 - 7 * x + 45 = 0

a: 3.0b: -7.0c: 45.0
d = b^2 - 4 * a * c = -7.0^2 - 4 * 3.0 * 45.0 = 49.0 - 540.0 = -491.00
!!! No roots.
"""
if __name__ == '__main__':
    from algorithms.quadr_eq import solve

    solve("3 * x^2 - 7 * x + 45 = 0")
