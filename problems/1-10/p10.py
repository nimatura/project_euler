"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from functions.divisibility import is_prime


result = 0
max_n = 2000000
for n in range(2, max_n):
    if is_prime(n):
        result += n
print(result)
# 142913828922
