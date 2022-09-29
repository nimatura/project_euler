"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left
to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37,
and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from functions.divisibility import is_prime


def get_truncatable_primes(how, memo=None):
    if memo is None:
        memo = [[2, 3, 5, 7]]
    # base case
    if not memo[-1]:
        ret = []
        for l in memo[1:-1]:
            ret.extend(l)
        return ret
    new_primes = []
    for p in memo[-1]:
        for d in range(1, 10):
            candidate = int(str(p) + str(d)) if how == 'lr' else int(str(d) + str(p))
            if is_prime(candidate):
                new_primes.append(candidate)
    memo.append(new_primes)
    return get_truncatable_primes(how, memo)


def is_truncatable_prime(p, how='lr'):
    p_str = str(p)
    if len(p_str) < 2:
        return False
    for i in range(len(p_str)):
        if how == 'lr' and not is_prime(int(p_str[:i + 1])):
            return False
        elif not is_prime(int(p_str[i:])):
            return False
    return True


lr_truncatable_primes = get_truncatable_primes(how='lr')
truncatable_primes = [p for p in lr_truncatable_primes if is_truncatable_prime(p, 'rl')]
result = sum(truncatable_primes)
print(truncatable_primes)
print(result)
# 748317
