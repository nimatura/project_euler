import math


def is_palindrome(l: list):
    half_length = int(len(l) / 2)
    for i in range(half_length):
        if l[i] != l[-(i + 1)]:
            return False
    return True


def is_pandigital(n, size=None, start_with_zero=False):
    n_str = str(n)
    if not size:
        size = len(n_str)
    digits = ''
    if start_with_zero:
        for i in range(size):
            digits += str(i)
    else:
        for i in range(1, size + 1):
            digits += str(i)
    for d in digits:
        if n_str.count(d) != 1:
            return False
    return True


def get_periodic_decimal(a, b):
    div = int(a / b)
    rest = a % b
    result = str(div)
    if rest == 0:
        return result
    decimals = ''
    memo = {}
    counter = 0
    while rest != 0:
        a = rest * 10
        div = int(a / b)
        rest = a % b
        if (div, rest) in memo.keys():  # is periodic
            decimals = decimals[:memo[div, rest]] + '(' + decimals[memo[div, rest]:] + ')'
            break
        else:
            memo[div, rest] = counter
            decimals += str(div)
            counter += 1
    result = result + ',' + decimals
    return result


def is_pentagonal(n):
    delta = (1 + 24 * n) ** .5
    if not delta.is_integer():
        return False
    delta = int(delta)
    return (1 + delta) % 6 == 0


def is_hexagonal(n):
    delta = (1 + 8 * n) ** .5
    if not delta.is_integer():
        return False
    delta = int(delta)
    return (1 + delta) % 4 == 0


def polygonal_number(k, n):
    if k == 3:  # triangle number
        return int(n * (n + 1) / 2)
    if k == 4:  # square number
        return n ** 2
    if k == 5:  # pentagonal number
        return int(n * (3 * n - 1) / 2)
    if k == 6:  # hexagonal number
        return n * (2 * n - 1)
    if k == 7:  # heptagonal number
        return int(n * (5 * n - 3) / 2)
    if k == 8:  # octagonal number
        return n * (3 * n - 2)


def get_continued_fraction(n):
    """
    Returns the continued fraction representation of n.
    """

    result = []

    root = n ** .5

    x = root
    int_part = int(math.floor(x))
    result.append(int_part)

    a = int_part
    b = n - int_part ** 2

    period = []
    period_end = 2 * int(math.floor(x))
    while True:
        x = (root + a) / b
        int_part = int(math.floor(x))
        period.append(int_part)

        if int_part == period_end:
            if is_palindrome(period[:-1]):
                break

        a = abs(a - b * int_part)
        b = (n - a ** 2) / b

    result.append(period)
    return result


def max_triangle_sum(i, j, tri, memo=None):
    if memo is None:
        memo = {}
    if (i, j) in memo.keys():
        return memo[i, j]
    if i == 0:
        memo[i, j] = tri[i][j]
        return memo[i, j]
    else:
        if 1 <= j <= i - 1:
            memo[i, j] = max([
                max_triangle_sum(i - 1, j, tri, memo=memo),
                max_triangle_sum(i - 1, j - 1, tri, memo=memo)
            ]) + tri[i][j]
        elif j == 0:
            memo[i, j] = max_triangle_sum(i - 1, j, tri, memo=memo) + tri[i][j]
        else:
            memo[i, j] = max_triangle_sum(i - 1, j - 1, tri, memo=memo) + tri[i][j]
        return memo[i, j]
