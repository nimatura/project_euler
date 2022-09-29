"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import numpy as np
from functions.divisibility import is_prime


target = 600851475143
result = 1
n = int(np.sqrt(target))  # largest possible factor
while n > 0:
    if is_prime(n) and target % n == 0:
        result = n
        break
    n -= 1
print(result)
# 6857
