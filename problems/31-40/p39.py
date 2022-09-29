"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions
for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import math


max_p = 1000
all_solutions = {}
for p in range(12, max_p + 1):
    solutions = []
    min_c = int(math.floor(p / 3)) + 1
    for c in range(min_c, p - 2):
        rest = p - c
        for a in range(1, int(math.ceil(rest / 2))):
            b = rest - a
            if a**2 + b**2 == c**2:
                solutions.append((a, b, c))
    if solutions:
        all_solutions[p] = solutions
max_p = None
max_sol = None
max_sol_len = 0
for p, sol in all_solutions.items():
    if len(sol) > max_sol_len:
        max_p = p
        max_sol = sol
        max_sol_len = len(sol)
result = max_p
print('%i: %s' % (max_p, max_sol))
print(result)
# 840
