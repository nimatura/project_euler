import math
import numpy as np
from itertools import combinations
from collections import defaultdict


def gcd(n, m):
    """
    Returns the greatest common denominator between n and m.
    """
    while m != 0:
        n, m = m, n % m
    return n


def is_prime(n):
    """
    Returns True if n is prime and False otherwise.
    """
    if n < 2:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    max_factor = int(np.sqrt(n))  # largest possible factor
    k = 5
    while k <= max_factor:
        if n % k == 0 or n % (k + 2) == 0:
            return False
        k += 6
    return True


def get_primes(n):
    """
    Sieve of Eratosthenes, get all primes up to n.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(n + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [p for p, v in enumerate(primes) if v]


def get_prime_factors(n):
    """
    Return the prime factors of n in dictionary form -> {prime: multiplicity}
    """
    result = defaultdict(int)
    aux = n
    for i in range(2, n + 1):
        while aux % i == 0:
            result[i] += 1
            aux /= i
        if i > aux:
            break
    return result


def get_prime_factors_up_to(n):
    """
    Return the prime factors of all integers from 1 to N in the form -> {number: {prime: multiplicity}}
    Uses a modified sieve of Eratosthenes algorithm. It's more efficient than calculating the prime factors of each
    number separately.
    """
    prime_factors = {}
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
            for j in range(i, n + 1, i):
                mul = 0
                aux = j
                while aux % i == 0:
                    mul += 1
                    aux /= i
                if j in prime_factors.keys():
                    prime_factors[j][i] = mul
                else:
                    prime_factors[j] = {i: mul}
    return prime_factors


def get_divisors(n, proper=False):
    """
    Returns a list with all divisors of n. If proper is True, returns the proper divisors, that is, ignores n.
    """
    prime_factors = get_prime_factors(n)
    prime_factors_list = []
    for p, m in prime_factors.items():
        for i in range(m):
            prime_factors_list.append(p)
    comb = []
    for i in range(1, len(prime_factors_list) + 1):
        comb.extend(combinations(prime_factors_list, i))
    divisors = [1]
    for c in comb:
        d = 1
        for p in c:
            d *= p
        divisors.append(d)
    result = list(set(divisors))
    if proper:
        result.remove(n)
    return result


def totient(n, primes=None):
    """
    Euler's Totient function. Returns the number of integers less than n which are relative primes to n (including 1).
    """
    if primes is None:
        primes = get_primes(n)
    div_primes = [p for p in primes if n % p == 0]
    result = n
    for p in div_primes:
        result *= (1 - 1 / p)
    return int(result)


def mobius(n):
    """
    Mobius function. Can be used to get the totient summary function, though it's more efficient to do so with a sieve
    to get all the prime factors of multiple numbers at once, as in get_prime_factors_up_to.
    """
    prime_factors = get_prime_factors(n)
    if any(m != 1 for m in prime_factors.values()):  # check for square divisors
        return 0
    elif len(prime_factors) % 2 == 0:
        return 1
    else:
        return -1


def totient_summatory(n):
    """
    Sum of all totient numbers from 1 to n. Uses the mobius function, though it's more efficient to do so with a sieve
    to get all the prime factors of multiple numbers at once, as in get_prime_factors_up_to.
    """
    result = 0
    for k in range(1, n + 1):
        result += mobius(k) * math.floor(n / k) ** 2
    result = (1 / 2) * (1 + result)
    return int(result)
