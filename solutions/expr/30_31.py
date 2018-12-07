"""
  ( 3 )  / ( sin ( 45 ) )  * 0
-------------------------------------------------

Compute individual results:
sin(45.0) => 0.85
3.0 / 0.85 => 3.53
3.53 * 0.0 => 0.0
Result: 0.00
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("  ( 3 )  / ( sin ( 45 ) )  * 0")
# -------------------------------------------------
