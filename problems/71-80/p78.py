"""
Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins
can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
"""


def update_partitions(k, a, p):
    if k in p:
        return p
    for l in range(1, k + 1):
        if l not in p.keys():
            p[l] = 0
            for m in range(1, l + 1):
                if m in a.keys():
                    p = update_partitions(l - m, a, p)
                    p[l] -= a[m] * p[l - m]
    return p


n = 100000

alpha = {0: 1}
r = 1
n1 = int(r * (3 * r - 1) / 2)
n2 = int(r * (3 * r + 1) / 2)
while n1 <= n:
    alpha[n1] = (-1) ** r
    alpha[n2] = (-1) ** r
    r += 1
    n1 = int(r * (3 * r - 1) / 2)
    n2 = int(r * (3 * r + 1) / 2)

result = None
partitions = {0: 1}
for i in range(4, n + 1, 5):
    if (i - 5) % 7 == 0 or (i - 6) % 11 == 0:
        pass
    partitions = update_partitions(i, alpha, partitions)
    if partitions[i] % 1000000 == 0:
        result = i
        break

print(result)
# 55374
