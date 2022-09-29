"""
Consider quadratic Diophantine equations of the form:

x2 – Dy2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
"""


from classes.numeric import RationalNumber
from functions.misc import get_continued_fraction

"""
Author's note:

This diophantine equation is called Pell's equation.

There's a way to find its fundamental solution via continued fractions. That is, the fundamental solution x, y is
actually a convergent when writen like x / y. Hence, the fundamental solution is the first convergent h_i / k_i that
satisfies the equation.
"""


def continued_fraction_to_convergent(continued_fraction, limit=None):
    is_periodic = len(continued_fraction) == 2 and isinstance(continued_fraction[1], list)
    if is_periodic:
        if not limit:
            raise ValueError('must specify a limit for periodic fractions!')
        coef = continued_fraction[:1]
        period_counter = 0
        coef_counter = 1
        while True:
            coef.append(continued_fraction[1][period_counter])
            period_counter += 1
            coef_counter += 1
            if period_counter >= len(continued_fraction[1]):
                period_counter = 0
            if coef_counter > limit:
                break
    else:
        coef = continued_fraction

    result = RationalNumber(0)
    for a in coef[::-1][:-1]:
        result = RationalNumber(1) / (RationalNumber(a) + result)
        # result = result.simplify()
    result = RationalNumber(coef[0]) + result
    return result


max_n = 1
max_x = 0
for n in range(2, 1001):
    if int(n ** .5) ** 2 == n:  # check for perfect square
        continue
    continued = get_continued_fraction(n)
    k = 1
    while True:
        convergent = continued_fraction_to_convergent(continued, limit=k)
        x = convergent.p
        y = convergent.q
        if x ** 2 - n * y ** 2 == 1:
            break
        k += 1
    if x > max_x:
        max_x = x
        max_n = n
    print('%i : %i' % (n, x))
print(max_n)
