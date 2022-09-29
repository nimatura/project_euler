"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
English words, how many are triangle words?
"""

from functions.text import alphabetical_value


def triangle_function(n):
    return (1 / 2) * n * (n + 1)


with open('../../data/p042_words.txt', 'r') as f:
    contents = f.read()

words = [n.strip('"').lower() for n in contents.split(',')]
alphabetical_values = []
for w in words:
    alphabetical_values.append(alphabetical_value(w))

max_value = max(alphabetical_values)

triangle_numbers = []
n = 1
while True:
    t_num = triangle_function(n)
    if t_num > max_value:
        break
    triangle_numbers.append(t_num)
    n += 1

result = 0
for val in alphabetical_values:
    if val in triangle_numbers:
        result += 1

print(result)
# 162
