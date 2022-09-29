"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a
square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from functions.divisibility import is_prime


def is_goldbach_number(n):
    max_k = int(((n - 3) / 2) ** .5)
    for k in range(1, max_k + 1):
        rest = n - 2 * k ** 2
        if is_prime(rest):
            return True
    return False


i = 1
while True:
    candidate = 2 * i + 1
    if not is_prime(candidate):  # must be composite
        if not is_goldbach_number(candidate):
            print(candidate)
            break
    i += 1
# 5777
