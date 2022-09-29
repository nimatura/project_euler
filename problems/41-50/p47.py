"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

from functions.divisibility import get_prime_factors


prime_factors_dict = {1: 0, 2: 1, 3: 1, 4: 1}
n = 5
while True:
    prime_factors = get_prime_factors(n)
    prime_factors_dict[n] = len(prime_factors.keys())
    if prime_factors_dict[n] >= 4 and prime_factors_dict[n - 1] >= 4 and prime_factors_dict[n - 2] >= 4\
            and prime_factors_dict[n - 3] >= 4:
        break
    n += 1

print(n - 3)
# 134043
