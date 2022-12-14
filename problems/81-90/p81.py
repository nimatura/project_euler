"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and
down, is indicated in bold red and is equal to 2427.

Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by
80 matrix, from the top left to the bottom right by only moving right and down.
"""
from functions.misc import min_square_sum


with open('../../data/p081_matrix.txt', 'r') as f:
    contents = f.read()

rectangle = contents.split('\n')[:-1]
rectangle = [[int(n) for n in row.split(',')] for row in rectangle]

rectangle_height = len(rectangle)
rectangle_width = len(rectangle[0])

result = min_square_sum(rectangle_height - 1, rectangle_width - 1, rectangle)

print(result)
# 427337
