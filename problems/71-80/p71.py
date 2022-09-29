"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper
fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the
fraction immediately to the left of 3/7.
"""

import math
from classes.numeric import RationalNumber


max_d = 1000000
pivot = RationalNumber(3, 7)
best_candidate = 0
best_difference = RationalNumber(1)
for d in range(2, max_d + 1):
    n = math.floor(d * 3 / 7)
    candidate = RationalNumber(n, d)
    difference = pivot - candidate
    if difference.p == 0:
        continue
    if difference < best_difference:
        best_candidate = candidate
        best_difference = difference
result = best_candidate.p
print(result)
# 428570
