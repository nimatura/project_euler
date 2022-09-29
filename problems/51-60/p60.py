"""
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
"""

import numpy as np
from functions.divisibility import is_prime


primes = []
max_p = 10000
for p in range(2, max_p + 1):
    if is_prime(p):
        primes.append(p)

print('%i primes found' % len(primes))
print('building remarkable pairs matrix')

remarkable_pairs = np.zeros((len(primes), len(primes)))

for i in range(len(primes)):
    for j in range(i):
        p1 = primes[i]
        p2 = primes[j]
        concat1 = int(str(p1) + str(p2))
        concat2 = int(str(p2) + str(p1))
        if concat1 in primes or (concat1 > primes[-1] and is_prime(concat1)):
            is_prime1 = True
        else:
            is_prime1 = False
        if concat2 in primes or (concat2 > primes[-1] and is_prime(concat2)):
            is_prime2 = True
        else:
            is_prime2 = False
        if is_prime1 and is_prime2:
            remarkable_pairs[i, j] = 1
            remarkable_pairs[j, i] = 1

'building remarkable pairs list'

remarkable_group_indexes = []
for i in range(len(primes)):
    for j in range(i):
        if remarkable_pairs[j, i] == 1:
            remarkable_group_indexes.append([j, i])

print('%i group(s) of size 2 found' % len(remarkable_group_indexes))

base = remarkable_group_indexes
for k in range(3, 6):
    print('expanding groups to size %i' % k)
    new_base = []
    for group in base:
        if group[-1] + 1 > len(primes):
            break
        for i in range(group[-1] + 1, len(primes)):
            is_remarkable_group = True
            for j in group:
                if remarkable_pairs[i, j] != 1:
                    is_remarkable_group = False
                    break
            if is_remarkable_group:
                new_base.append(group + [i])
    print('%i group(s) of size %i found' % (len(new_base), k))
    base = new_base
remarkable_groups = [[primes[i] for i in g] for g in base]

remarkable_groups = [(g, sum(g)) for g in remarkable_groups]
remarkable_groups = sorted(remarkable_groups, key=lambda x: x[1])
result = remarkable_groups[0][1]
print(result)
#
