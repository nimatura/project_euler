"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers
less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine
and relatively prime to nine, φ(9)=6. The number 1 is considered to be relatively prime to every positive number, so
φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 107, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
"""


from functions.divisibility import get_primes
from functions.text import is_anagram

"""
Author's Note:

This solution rests in an observation similar to the one used in problem 69: if n is prime, then n / φ(n) is lesser or
equal than m / φ(m) for all m < n.

The problem with this is if n is prime, then φ(n) = n - 1, which can't be an anagram of n. So we'll use the next best
option, n = p1 * p2, where p1 and p2 are primes.
"""


primes = get_primes(10000)

prime_products = []
for i, p1 in enumerate(primes):
    for j, p2 in enumerate(primes[i:]):
        n = p1 * p2
        if n > 10000000:
            break
        phi_n = int(n * (1 - 1 / p1) * (1 - 1 / p2))
        n_over_phi = n / phi_n
        if is_anagram(str(n), str(phi_n)):
            prime_products.append((n, phi_n, n_over_phi))


result = min(prime_products, key=lambda x: x[2])
print(result[0])
# 8319823
