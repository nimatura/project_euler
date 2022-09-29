"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product
of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with
(1,2, ... , n) where n > 1?
"""


from functions.misc import is_pandigital


def concatenated_product(x, tup):
    prod = ''
    for t in tup:
        prod += str(x * t)
    return int(prod)


result = 123456789
n_ranges = {1: 8, 2: 5, 3: 4, 4: 3, 5: 2}
for k_digits in n_ranges.keys():
    for k in range(10 ** (k_digits - 1), 10 ** k_digits):
        for n in range(2, n_ranges[k_digits] + 1):
            concat_prod = concatenated_product(k, tuple(range(n)))
            if concat_prod > result and is_pandigital(concat_prod, 9):
                result = concat_prod
print(result)
# 932718654
