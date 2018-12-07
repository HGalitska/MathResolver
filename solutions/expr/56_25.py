"""
  ( 5 + sqrt ( 25 ) )  - ( 4 + 3 + floor ( 6.4 ) )  * 21

Compute individual results:
sqrt(25.0) => 5.0
5.0 + 5.0 => 10.0
4.0 + 3.0 => 7.0
floor(6.4) => 6.0
7.0 + 6.0 => 13.0
13.0 * 21.0 => 273.0
10.0 - 273.0 => -263.0
Result: -263.00
"""
if __name__ == '__main__':
    from algorithms.expr import solve

    solve("  ( 5 + sqrt ( 25 ) )  - ( 4 + 3 + floor ( 6.4 ) )  * 21")