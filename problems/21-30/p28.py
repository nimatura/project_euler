"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

import numpy as np
from classes.iterators import Spiral


r = 500
s = Spiral(center=(r, r), ratio=r)
mx = np.zeros((2 * r + 1, 2 * r + 1))
counter = 1
for i, j in iter(s):
    mx[i, j] = counter
    counter += 1

sum_diag1 = 0
sum_diag2 = 0
for k in range(2 * r + 1):
    sum_diag1 += mx[k, k]
    sum_diag2 += mx[k, 2 * r - k]
result = int(sum_diag1 + sum_diag2 - mx[r, r])
print(result)
# 669171001
