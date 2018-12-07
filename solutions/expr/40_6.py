"""
  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 1
-------------------------------------------------

Compute individual results:
sqrt(36.0) => 6.0
sin(45.0) => 0.85
6.0 / 0.85 => 7.06
7.06 * 1.0 => 7.06
Result: 7.06
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("  ( sqrt ( 36 ) )  / ( sin ( 45 ) )  * 1")
# -------------------------------------------------
