"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper
fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
"""

from functions.divisibility import gcd


max_d = 12000
min_value = 1 / 3
max_value = 1 / 2
result = 0
for d in range(2, max_d + 1):
    for n in range(1, d):
        if min_value < n / d < max_value and gcd(n, d) == 1:
            result += 1
print(result)
# 7295372
