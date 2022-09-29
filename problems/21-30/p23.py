"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from functions.divisibility import get_divisors


max_n = 28123
abundant_numbers = []
for n in range(12, max_n + 1):
    div = get_divisors(n, proper=True)
    if n < sum(div):  # check if n is abundant
        abundant_numbers.append(n)

sum_of_abundant = set()
for i in range(len(abundant_numbers)):
    for j in range(i, len(abundant_numbers)):
        n = abundant_numbers[i]
        m = abundant_numbers[j]
        n_plus_m = n + m
        if n_plus_m <= max_n:
            sum_of_abundant.add(n + m)
not_sum_of_abundant = set(range(1, max_n + 1)).difference(sum_of_abundant)
result = sum(not_sum_of_abundant)
print(result)
# 4179871
