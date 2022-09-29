"""
Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this
example), each solution can be described uniquely. For example, the above solution can be described by the set:
4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

Total	Solution Set
9	4,2,3; 5,3,1; 6,1,2
9	4,3,2; 6,2,1; 5,1,3
10	2,3,5; 4,5,1; 6,1,3
10	2,5,3; 6,3,1; 4,1,5
11	1,4,6; 3,6,2; 5,2,4
11	1,6,4; 5,4,2; 3,2,6
12	1,5,6; 2,6,4; 3,4,5
12	1,6,5; 3,5,4; 2,4,6
By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the
maximum 16-digit string for a "magic" 5-gon ring?
"""
import numpy as np
from itertools import permutations


def compact_to_extended_ring(cr):
    assert len(cr) % 2 == 0
    n = int(len(cr) / 2)
    ring = np.zeros((n, 3))
    ring[:, 0] = np.array(cr[:int(len(cr) / 2)])
    ring[:, 1] = np.array(cr[int(len(cr) / 2):])
    ring[:-1, 2] = np.array(cr[int(len(cr) / 2 + 1):])
    ring[-1, 2] = np.array(cr[int(len(cr) / 2)])
    return ring


def is_magic_ring(r):
    row_sum = np.sum(r, axis=1)
    return (row_sum == row_sum[0]).all()


def extended_ring_to_key(r):
    min_row = np.argmin(r[:, 0])
    ordered_ring = np.zeros(r.shape)
    ordered_ring[:r.shape[0] - min_row, :] = r[min_row:, :]
    ordered_ring[r.shape[0] - min_row:, :] = r[:min_row]
    key = ''.join([''.join([str(int(d)) for d in row]) for row in ordered_ring])
    return key


n_digits = 10
digits = list(range(1, n_digits + 1))
magic_rings = []
for p in permutations(digits):
    compact_ring = [d for d in p]
    extended_ring = compact_to_extended_ring(compact_ring)
    if is_magic_ring(extended_ring):
        magic_rings.append(extended_ring)

magic_rings_keys = [extended_ring_to_key(r) for r in magic_rings]
magic_rings_keys = list(set(magic_rings_keys))
magic_rings_keys = sorted([int(k) for k in magic_rings_keys if len(str(k)) == 16], reverse=True)
print(magic_rings_keys[0])
# 6531031914842725
