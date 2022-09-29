"""
Note from the author:

There's a property of continued fractions of sqrt(n) which states that: starting from 2, the period of the first 2
numbers (2 and 3) end with a 2, the next 4 end with a 4, the next 6 with a 6 and so on. Another property is that the
period before the last number is a palindrome.

I won't prove this properties here. However, they're quite useful as stop conditions, otherwise we might run into
precision errors.
"""
from functions.misc import get_continued_fraction


n_odd_periods = 0
for k in range(2, 10001):
    if int(k ** .5) ** 2 == k:  # check for perfect square
        continue
    continued_fraction = get_continued_fraction(k)
    print('%i (%i): %s' % (k, len(continued_fraction[1]), continued_fraction))
    if len(continued_fraction[1]) % 2 == 1:
        n_odd_periods += 1
print(n_odd_periods)
# 1322
