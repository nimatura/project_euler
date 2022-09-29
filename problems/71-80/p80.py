"""
It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal
expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits
for all the irrational square roots.
"""

from decimal import getcontext
from functions.optimization import newton_raphson


getcontext().prec = 105


def dp(x):
    return 2 * x


total_sum = 0
for n in range(2, 101):

    def p(x):
        return x ** 2 - n

    zero = newton_raphson(p, dp, x0=1, max_iter=100, tol=1e-100)
    if zero == int(zero):
        continue

    decimals = str(zero).replace('.', '')[:100]

    partial_sum = 0
    for d in decimals:
        partial_sum += int(d)

    total_sum += partial_sum

print(total_sum)
# 40886
