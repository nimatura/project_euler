"""
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many ways can one hundred be written as a sum of at least two positive integers?
"""

from functions.combinatory import n_partitions


result = n_partitions(100) - 1
print(result)
# 190569291
