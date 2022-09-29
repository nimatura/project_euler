"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and,
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from functions.divisibility import is_prime
from functions.text import is_anagram
from itertools import combinations


primes = []
for n in range(1000, 10000):
    if is_prime(n):
        primes.append(n)

groups = []
for p in primes:
    is_new = True
    for g in groups:
        if is_anagram(str(p), str(g[-1])):
            g.append(p)
            is_new = False
    if is_new:
        groups.append([p])

for g in groups:
    comb3 = sorted(list(combinations(g, 3)))
    for c in comb3:
        if (c[0] - c[1]) == (c[1] - c[2]):
            print(''.join([str(n) for n in c]))
# 296962999629
