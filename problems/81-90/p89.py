
with open('../../data/p089_roman.txt', 'r') as f:
    contents = f.read()

roman_numbers = [n for n in contents.split('\n')[:-1]]
print(roman_numbers)
