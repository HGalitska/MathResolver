"""
  ( 5 + sqrt ( 25 ) )  - ( 4 + 3 + floor ( 6.4 ) )  * 1

Compute individual results:
sqrt(25.0) => 5.0
5.0 + 5.0 => 10.0
4.0 + 3.0 => 7.0
floor(6.4) => 6.0
7.0 + 6.0 => 13.0
13.0 * 1.0 => 13.0
10.0 - 13.0 => -3.0
Result: -3.00
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("  ( 5 + sqrt ( 25 ) )  - ( 4 + 3 + floor ( 6.4 ) )  * 1")