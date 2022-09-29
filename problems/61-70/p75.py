"""
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in
exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other
lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three
different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle
triangle be formed?
"""

from functions.divisibility import gcd


pythagorean_triples_by_length = {}
max_L = 1500000

max_k = int(max_L / 6)
for k in range(1, max_k + 1):  # ranges are set so that L never goes over max_l
    max_m = int((-1 + (1 + 4 * max_L / k) ** .5) / 2)
    for m in range(2, max_m + 1):
        max_n = min(m, int(max_L / (2 * m * k) - m))
        for n in range(1, max_n + 1):
            if m % 2 == 1 and n % 2 == 1:  # n and m can't be both odd
                continue
            if gcd(n, m) != 1:  # n and m must be co-prime
                continue
            a = k * (m ** 2 - n ** 2)
            b = k * (2 * m * n)
            c = k * (m ** 2 + n ** 2)
            L = a + b + c
            if L in pythagorean_triples_by_length:
                pythagorean_triples_by_length[L].add(c)
            else:
                pythagorean_triples_by_length[L] = {c}

result = 0
max_L = 0
for L, s in pythagorean_triples_by_length.items():
    if len(s) == 1:
        result += 1
    if L > max_L:
        max_L = L
print(max_L)
print(result)
# 497397
