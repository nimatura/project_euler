"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the numbers from 1 to 20?
"""
from functions.divisibility import get_prime_factors
from collections import defaultdict


result_prime_factors = defaultdict(int)
for i in range(2, 21):
    i_prime_factors = get_prime_factors(i)
    for p, m in i_prime_factors.items():
        if m > result_prime_factors[p]:
            result_prime_factors[p] = m

result = 1
for p, m in result_prime_factors.items():
    result *= p**m
print(result)
