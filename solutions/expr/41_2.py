"""
  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 12
-------------------------------------------------

Compute individual results:
sqrt(36.0) => 6.0
sin(45.0) => 0.85
6.0 / 0.85 => 7.06
7.06 * 12.0 => 84.72
Result: 84.72
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 12")
# -------------------------------------------------
