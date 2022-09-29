"""
Author's note:

It's assumed, according to the enunciate, that e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...]
"""

from classes.numeric import RationalNumber


def continued_fraction_e(k):
    result = [2, 1, 2]
    for i in range(2, k + 1):
        result.extend([1, 1, 2 * i])
    return result


def continued_fraction_to_convergent(continued_fraction):
    result = RationalNumber(0)
    for a in continued_fraction[::-1][:-1]:
        result = RationalNumber(1) / (RationalNumber(a) + result)
        # result = result.simplify()
    result = RationalNumber(continued_fraction[0]) + result
    return result


e = continued_fraction_e(34)[:-2]
print(len(e))
convergent = continued_fraction_to_convergent(e)
print(convergent)
digit_sum = sum(int(d) for d in str(convergent.p))
print(digit_sum)
# 272
