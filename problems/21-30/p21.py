"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


from functions.divisibility import get_divisors


max_n = 10000
memo = []
amicable_pairs = []
for n in range(1, max_n + 1):
    if n in memo:
        continue
    proper_divisors = get_divisors(n)
    proper_divisors.remove(n)
    divisors_sum = sum(proper_divisors) if proper_divisors else 0
    if 0 < divisors_sum <= max_n:
        proper_divisors_2 = get_divisors(divisors_sum)
        proper_divisors_2.remove(divisors_sum)
        divisors_sum_2 = sum(proper_divisors_2)
        if divisors_sum_2 == n and n != divisors_sum and [divisors_sum, n] not in amicable_pairs:
            amicable_pairs.append([n, divisors_sum])

result = sum([sum(pair) for pair in amicable_pairs])
print(amicable_pairs)
print(result)
# 31626
