"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
from functions.text import is_palindrome


result = 1
two_digit_products = []
for i in range(1, 999):
    for j in range(1, 999):
        two_digit_products.append(i * j)
two_digit_products = sorted(two_digit_products, reverse=True)
for n in two_digit_products:
    if is_palindrome(str(n)):
        result = n
        break
print(result)
