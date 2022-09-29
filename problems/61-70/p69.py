"""
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than
n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to
nine, φ(9)=6.

n	Relatively Prime	φ(n)	n / φ(n)
2	1                   1	    2
3	1,2                 2	    1.5
4	1,3                 2	    2
5	1,2,3,4	            4	    1.25
6	1,5	                2	    3
7	1,2,3,4,5,6	        6	    1.1666...
8	1,3,5,7	            4	    2
9	1,2,4,5,7,8	        6	    1.5
10	1,3,7,9	            4	    2.5
It can be seen that n=6 produces a maximum n / φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n / φ(n) is a maximum.
"""


from functions.divisibility import get_primes, totient

"""
Author's Note:

This solution rests in the following conjecture: if n = p1 * p2 * ... * pk where p1, p2, ..., pk are the first k
primes, then n / φ(n) is greater or equal than m / φ(m) for all m < n.

If this is true, then it's enough to find the biggest product of consecutive primes (starting from 2) that's lesser or
equal than 1,000,000.

The proof to this conjecture can be derived from the function's closed form, and is left as an exercise for the reader
:P.
"""


primes = get_primes(1000)
candidate = 1
for p in primes:
    if p * candidate > 1000000:
        break
    else:
        candidate *= p
print('%i - %i - %0.2f' % (candidate, totient(candidate), candidate / totient(candidate)))
