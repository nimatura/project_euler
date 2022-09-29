"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""

from functions.divisibility import get_primes
from classes.algebraic import Polynomial
from pprint import pprint


n = 100
primes = get_primes(n)

n_sieves = []
for p in primes:
    p_sieve = Polynomial()
    i = 0
    prod = i * p
    while prod < n:
        p_sieve.coef[prod] = 1
        i += 1
        prod = i * p
    n_sieves.append(p_sieve)
product = n_sieves[0]
for sieve in n_sieves[1:]:
    product *= sieve

result = None
for k in sorted(product.coef.keys()):
    if product.coef[k] > 5000:
        result = k
        break
print(result)
# 71
