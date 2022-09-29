"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1
through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from itertools import permutations


digits = '123456789'
unusual_numbers = []
# it can be proven 1d * 4d = 4d and 2d * 3d = 4d are the only valid combinations that use all 9 digits in a product
digit_permutations = list(permutations(digits))
for p in digit_permutations:
    # 1d * 4d = 4d
    n1 = int(p[0])
    n2 = int(''.join(p[1:5]))
    n3 = int(''.join(p[5:]))
    if n1 * n2 == n3:
        unusual_numbers.append(n3)
    # 2d * 3d = 4d
    n1 = int(''.join(p[:2]))
    n2 = int(''.join(p[2:5]))
    if n1 * n2 == n3:
        unusual_numbers.append(n3)

unusual_numbers = list(set(unusual_numbers))
result = sum(unusual_numbers)
print(unusual_numbers)
print(result)
# 45228
