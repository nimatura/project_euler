"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one
followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

max_digits = 0
for a in range(1, 100):
    for b in range(1, 100):
        power = a ** b
        n_digits = sum(int(d) for d in str(power))
        if n_digits > max_digits:
            max_digits = n_digits
print(max_digits)
