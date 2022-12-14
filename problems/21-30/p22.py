"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

from functions.text import alphabetical_value


with open('../../data/p022_names.txt', 'r') as f:
    contents = f.read()

names = [n.strip('"').lower() for n in contents.split(',')]
ordered_names = sorted(names)

result = 0
for i, name in enumerate(ordered_names):
    name_score = (i + 1) * alphabetical_value(name)
    result += name_score
print(result)
# 871198282
