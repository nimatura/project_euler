"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""


def n_paths(x, y, memo=None):
    if memo is None:
        memo = {}
    if (x, y) in memo.keys():
        return memo[x, y]
    if x == 0 or y == 0:
        memo[x, y] = 1
        return memo[x, y]
    else:
        memo[x, y] = n_paths(x - 1, y, memo=memo) + n_paths(x, y - 1, memo=memo)
        return memo[x, y]


print(n_paths(20, 20))
# 137846528820
