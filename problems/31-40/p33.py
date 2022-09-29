"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from classes.numeric import RationalNumber


curious_fractions = []
for p in range(10, 100):
    for q in range(p + 1, 100):
        div = p / q
        p_str = str(p)
        q_str = str(q)
        for p_digit in p_str:
            if p_digit in q_str:
                common_digit = p_digit
                if int(common_digit) == 0:  # trivial case
                    continue
                new_p_str = p_str.replace(common_digit, '', 1)
                new_q_str = q_str.replace(common_digit, '', 1)
                if int(new_q_str) == 0:
                    continue
                dummy_div = int(new_p_str) / int(new_q_str)
                if div == dummy_div:
                    curious_fractions.append((p, q))
                break
print(curious_fractions)

simplified_fractions = []
for p, q in curious_fractions:
    simplified = RationalNumber(p, q).simplify()
    simplified_fractions.append((simplified.p, simplified.q))
print(simplified_fractions)

result = 1
for p, q in simplified_fractions:
    result *= q
print(result)
# 980
