"""
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

"""
Author's note:

Since 10^n has n + 1 digits, any base greater than 10 to the power of n will have more than n digits. That means we only
have to check bases from 1 to 9.

Also, if a is a number between 2 and 9, and a^n has less than n digits, then a^(n + 1) will also have less than n + 1
digits. That's because multiplying by a can't add more than 1 digit since a is less than 10.

This means we only have to iteratively check every number from 2 to 9 and every exponent until the property stops being
true (note that if the exponent is 1 the property is always true).
"""


result = 0
for a in range(1, 10):
    n = 1
    while len(str(a ** n)) == n:
        print('%i^%i = %i' % (a, n, a ** n))
        result += 1
        n += 1

print(result)
# 49
