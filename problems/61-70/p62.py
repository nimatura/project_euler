"""
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact,
41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

from functions.text import is_anagram


cubes = []
for n in range(1, 10000):
    cubes.append(n ** 3)

# group by anagrams
anagram_groups = []

for c in cubes:
    has_group = False
    for group in anagram_groups:
        if all(is_anagram(str(c), str(g)) for g in group):
            group.append(c)
            has_group = True
            break
    if not has_group:
        anagram_groups.append([c])

result = 0
for group in anagram_groups:
    if len(group) >= 5:
        result = group[0]
        break

print(result)
# 140283769536
