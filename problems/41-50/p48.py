"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""


result = 0
for i in range(1, 1001):
    result += i ** i
result = str(result)[-10:]
print(result)
