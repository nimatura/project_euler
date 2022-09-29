"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""


from itertools import permutations
from functions.combinatory import factorial

"""
Author's Note:

Note that an eight digit number is at least 10^7. But the sum of the factorial of its numbers is at most
8 * 9! = 2903040, hence it can't be a curious number. So an upper bound for these numbers is 2903041.
"""

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
digit_factorials = {}
for d in digits:
    digit_factorials[d] = factorial(d)

upper_bound = 2903041
curious_numbers = []
for i in range(10, upper_bound):
    sorted_digits = sorted([d for d in str(i)], reverse=True)
    factorial_sum = 0
    for d in sorted_digits:
        factorial_sum += digit_factorials[int(d)]
        if factorial_sum > i:
            break
    if factorial_sum == i:
        curious_numbers.append(i)

result = sum(curious_numbers)
print(curious_numbers)
print(result)
# 40730
