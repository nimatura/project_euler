"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from functions.combinatory import factorial


n = 100
fac_n = factorial(n)
fac_n_str = str(fac_n)
result = 0
for d in fac_n_str:
    result += int(d)
print(result)
