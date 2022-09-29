def factorial(n: int):
    assert n >= 0, 'n must be a non-negative integer'
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def n_permutations(n: int, k: int):
    assert n >= k, 'n must be greater or equal than k'
    return int(factorial(n) / factorial(n - k))


def n_combinations(n: int, k: int):
    return int(n_permutations(n, k) / factorial(k))


def consecutive_combinations(ordered_collection, k):
    assert(k <= len(ordered_collection))
    comb = []
    for i in range(len(ordered_collection) - k + 1):
        comb.append(ordered_collection[i: k + i])
    return iter(comb)


def n_partitions(n):
    """
    Euler's recurrence to get the number of partitions an integer has.
    """
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
    partitions = {0: 1}
    for i in range(1, n + 1):
        partitions[i] = 0
        for j in range(1, i + 1):
            partitions[i] -= alpha.get(j, 0) * partitions[i - j]
    return partitions[n]
