"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from functions.divisibility import is_prime


primes = []
max_n = 1000000
for n in range(1, max_n + 1):
    if is_prime(n):
        primes.append(n)

print(len(primes))

longest_sum = []
for start in range(len(primes)):
    if primes[start] * len(longest_sum) > primes[-1]:
        break
    end = min(start, len(primes) - 1)
    partial_sum = []
    while sum(partial_sum) < primes[-1] and end < len(primes):
        partial_sum = primes[start: end]
        if sum(partial_sum) in primes and len(partial_sum) > len(longest_sum):
            longest_sum = partial_sum
        end += 1

print(sum(longest_sum))
# 997651
