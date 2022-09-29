"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example,
2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from itertools import permutations
from functions.divisibility import is_prime


pand = []
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in range(1, 10):
    n_pand_tup = list(permutations(digits[:n]))
    n_pand = []
    for tup in n_pand_tup:
        pand_str = ''
        for t in tup:
            pand_str += str(t)
        n_pand.append(int(pand_str))
    pand.extend(n_pand)

result = None
for p in pand[::-1]:
    if is_prime(p):
        result = p
        break
print(result)
# 7652413
