"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

from classes.iterators import ChampernowneConstant


digits = []
positions = [1, 10, 100, 1000, 10000, 100000, 1000000]
c = ChampernowneConstant()
pos = 1
for d in iter(c):
    if pos in positions:
        digits.append(d)
    pos += 1
    if pos > positions[-1]:
        break

result = 1
for d in digits:
    result *= d
print(digits)
print(result)
# 210
