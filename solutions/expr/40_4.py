"""
  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 4
-------------------------------------------------

Compute individual results:
sqrt(25.0) => 5.0
sin(45.0) => 0.85
5.0 / 0.85 => 5.88
5.88 * 4.0 => 23.52
Result: 23.52
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("  ( sqrt ( 25 ) )  / ( sin ( 45 ) )  * 4")
# -------------------------------------------------
