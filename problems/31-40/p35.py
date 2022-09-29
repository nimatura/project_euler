"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves
prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""


from functions.divisibility import is_prime


def get_rotations(n):
    rotations = [n]
    aux = str(n)
    for i in range(len(str(n)) - 1):
        aux = aux[1:] + aux[0]
        rotations.append(int(aux))
    return rotations


circular_primes = []
for n in range(2, 1000000):
    if n in circular_primes:
        continue
    n_rotations = get_rotations(n)
    all_primes = True
    for r in n_rotations:
        if not is_prime(r):
            all_primes = False
            break
    if all_primes:
        circular_primes.append(n)

result = len(circular_primes)
print(result)
# 55
