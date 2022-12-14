"""
Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are
generated by the following formulae:

Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.

The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the
last number with the first).
Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a
different number in the set.
This is the only set of 4-digit numbers with this property.
Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square,
pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.
"""

from itertools import permutations
from functions.misc import polygonal_number


polygonal_numbers = []
for k in range(3, 9):
    print('generating %i-polygonal numbers' % k)
    k_polygonal_numbers = []
    n = 1
    while True:
        p_number = polygonal_number(k, n)
        if p_number < 1000:
            n += 1
            continue
        if p_number > 10000:
            break
        k_polygonal_numbers.append(p_number)
        n += 1
    print('found %i %i-polygonal numbers' % (len(k_polygonal_numbers), k))
    polygonal_numbers.append(k_polygonal_numbers)


chain = None
for perm in permutations(range(len(polygonal_numbers))):
    chain = []
    for n0 in polygonal_numbers[perm[0]]:
        chain.append(n0)
        for n1 in polygonal_numbers[perm[1]]:
            if str(chain[-1])[2:] == str(n1)[:2]:
                chain.append(n1)
                for n2 in polygonal_numbers[perm[2]]:
                    if str(chain[-1])[2:] == str(n2)[:2]:
                        chain.append(n2)
                        for n3 in polygonal_numbers[perm[3]]:
                            if str(chain[-1])[2:] == str(n3)[:2]:
                                chain.append(n3)
                                for n4 in polygonal_numbers[perm[4]]:
                                    if str(chain[-1])[2:] == str(n4)[:2]:
                                        chain.append(n4)
                                        for n5 in polygonal_numbers[perm[5]]:
                                            if str(chain[-1])[2:] == str(n5)[:2] and str(n5)[2:] == str(chain[0])[:2]:
                                                chain.append(n5)
                                                break
                                        if len(chain) < 6:
                                            chain = chain[:-1]
                                        elif len(chain) == 6:
                                            break
                                if len(chain) < 5:
                                    chain = chain[:-1]
                                elif len(chain) == 6:
                                    break
                        if len(chain) < 4:
                            chain = chain[:-1]
                        elif len(chain) == 6:
                            break
                if len(chain) < 3:
                    chain = chain[:-1]
                elif len(chain) == 6:
                    break
        if len(chain) < 2:
            chain = chain[:-1]
        elif len(chain) == 6:
            break
    if chain:
        break

print(chain)
print(sum(chain))
