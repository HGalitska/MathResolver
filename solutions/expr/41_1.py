"""
  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 11
-------------------------------------------------

Compute individual results:
sqrt(36.0) => 6.0
sin(45.0) => 0.85
6.0 / 0.85 => 7.06
7.06 * 11.0 => 77.66
Result: 77.66
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 11")
# -------------------------------------------------
