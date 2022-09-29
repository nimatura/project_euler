"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""


"""
Author's Note:

It can be proven that a number of 7 digits, where the first digit is greater than 0, is always greater than the sum of
fifth powers of its digits. So we only need to iterate up to 999999.

Demonstration:
Let n be a 7 digit number. Then:
    n >= 10^6
      >= 10 * 10^5
      >  7 * 10^5
      > d1^5 + d2^5 + d3^5 + d4^5 + d5^5 + d6^5 + d7^5
"""

special_numbers = []
max_n = 1000000
power = 5
for n in range(10, max_n):
    power_sum = 0
    for d in str(n):
        power_sum += int(d) ** power
    if n == power_sum:
        special_numbers.append(n)
result = sum(special_numbers)
print(result)
# 443839
