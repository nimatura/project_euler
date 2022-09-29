"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53,
73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven
primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently, 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is
part of an eight prime value family.
"""

from functions.divisibility import is_prime
from itertools import combinations


primes = []
max_n = 1000000
for n in range(2, max_n + 1):
    if is_prime(n):
        primes.append(n)

print('%i primes found' % len(primes))

best_primes = []
for n in primes:
    if best_primes:
        break
    n_list = [int(c) for c in str(n)]
    comb = []
    for k in range(1, len(n_list) + 1):
        comb.extend(list(combinations(range(len(n_list)), k)))
    for c in comb:
        gen_primes = []
        n_list_copy = n_list.copy()
        iter_digits = range(1, 10) if 0 in c else range(10)
        for d in iter_digits:
            for i in c:
                n_list_copy[i] = d
            new_n = int(''.join([str(d) for d in n_list_copy]))
            if is_prime(new_n):
                gen_primes.append(new_n)
        if len(gen_primes) == 8:
            best_primes = gen_primes
print(best_primes[0])
# 121313
