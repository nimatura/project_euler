"""
The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""


from functions.text import is_palindrome
from classes.numeric import BinaryNumber


palindromes = []
for n in range(1, 1000000):
    bin_n = BinaryNumber(n)
    if is_palindrome(str(n)) and is_palindrome(bin_n.bin):
        palindromes.append(n)
result = sum(palindromes)
print(result)
# 872187
