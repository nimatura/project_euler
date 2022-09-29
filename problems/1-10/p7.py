"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from functions.divisibility import is_prime


number = 2
counter = 1
result = 0
while counter <= 10001:
    if is_prime(number):
        result = number
        counter += 1
    number += 1
print(result)
# 83233
