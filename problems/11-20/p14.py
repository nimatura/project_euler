"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""


def next_collatz(n):
    if n % 2 == 0:
        return int(n / 2)
    else:
        return int(3 * n + 1)


max_length = 0
max_k = 1000000
memory = {}
for k in range(1, max_k):
    collatz_seq_len = 1
    aux = k
    while aux != 1:
        aux = next_collatz(aux)
        if aux in memory.keys():
            collatz_seq_len += memory[aux]
            break
        else:
            collatz_seq_len += 1
    memory[k] = collatz_seq_len
    if collatz_seq_len > max_length:
        max_length = collatz_seq_len
print(max_length)
# 837799
