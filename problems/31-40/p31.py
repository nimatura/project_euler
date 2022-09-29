"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""


coins_ = [200, 100, 50, 20, 10, 5, 2, 1]
value_ = 200


def get_coin_combinations(coins, value):
    # base cases
    if value == 0:
        return 1
    if len(coins) == 1:
        if value % coins[0] == 0:
            return 1
        else:
            return 0
    # recursion
    n_combinations = 0
    for i in range(value // coins[0] + 1):
        rest = value - (coins[0] * i)
        n_combinations += get_coin_combinations(coins[1:], rest)
    return n_combinations


result = get_coin_combinations(coins_, value_)
print(result)
# 73682
