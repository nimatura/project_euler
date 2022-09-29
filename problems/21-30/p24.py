"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import math
from functions.combinatory import factorial


"""
(Author's note)

This one can be resolved "mathematically":

After ordering, there are exactly 9! permutations that start with each digit. Since 9! = 362880, that means the first 
digit is floor(1000000 / 362880) = 2.

Fixating the first digit, there are 8! permutations for each digit in the second place. Since 8! = 40320, and there are 
1000000 - 2 * 362880 = 274240 numbers left, that means the second digit is the one in the place:
floor(274240 / 40320) = 6, from the ones remaining. That is, the second digit is 5.

And so on...
"""

n_elements = 10
elements = list(range(n_elements))
rest = 999999
result = ''
for i in range(n_elements):
    fac = factorial(n_elements - i - 1)
    pos = math.floor(rest / fac)
    d = elements[pos]
    elements.remove(d)
    rest -= pos * fac
    result += str(d)
print(result)
# 2783915460
