"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different
order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

from functions.text import is_anagram


result = 0
multiples = range(2, 7)
n = 1
while True:
    if all([is_anagram(str(n), str(n * m)) for m in multiples]):
        result = n
        break
    n += 1
print(result)
# 142857
