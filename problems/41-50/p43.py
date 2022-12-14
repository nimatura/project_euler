"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""


from itertools import permutations


def is_interesting(n):
    if int(str(n)[1:4]) % 2 != 0:
        return False
    elif int(str(n)[2:5]) % 3 != 0:
        return False
    elif int(str(n)[3:6]) % 5 != 0:
        return False
    elif int(str(n)[4:7]) % 7 != 0:
        return False
    elif int(str(n)[5:8]) % 11 != 0:
        return False
    elif int(str(n)[6:9]) % 13 != 0:
        return False
    elif int(str(n)[7:10]) % 17 != 0:
        return False
    return True


some_primes = [2, 3, 5, 7, 11, 13, 17]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
interesting_pand = []
for tup in iter(permutations(digits, len(digits))):
    if tup[0] == 0:
        continue
    pand_str = ''
    for t in tup:
        pand_str += str(t)
    pand = int(pand_str)
    if is_interesting(pand):
        interesting_pand.append(pand)

result = sum(interesting_pand)
print(result)
# 16695334890
