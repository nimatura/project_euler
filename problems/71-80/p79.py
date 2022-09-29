"""
A common security method used for online banking is to ask the user for three random characters from a passcode. For
example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be:
317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible
secret passcode of unknown length.
"""


def attempt_to_condition(a):
    condition = []
    s_digits = [d for d in str(a)]
    for i, d1 in enumerate(s_digits):
        for d2 in s_digits[i + 1:]:
            condition.append((int(d1), int(d2)))
    return condition


with open('../../data/p079_keylog.txt', 'r') as f:
    contents = f.read()

attempts = [int(a) for a in contents.split('\n')[:-1]]

cond = []
for a in attempts:
    cond.extend(attempt_to_condition(a))
cond = sorted(list(set(cond)))

password = [cond[0][0], cond[0][1]]
for c in cond[1:]:
    if c[0] in password:
        pos0 = password.index(c[0])
        if c[1] in password:
            pos1 = password.index(c[1])
            if pos1 > pos0:
                pass
            else:
                if tuple([c[1], c[0]]) in cond:
                    password.append(c[1])
                else:
                    if pos1 > pos0:
                        password.pop(pos1)
                        password.pop(pos0)
                        password.insert(pos0, c[1])
                        password.insert(pos1, c[0])
                    else:
                        password.pop(pos0)
                        password.pop(pos1)
                        password.insert(pos1, c[0])
                        password.insert(pos0, c[1])
        else:
            password.append(c[1])
    else:
        if c[1] in password:
            password.insert(0, c[0])
        else:
            password.extend(list(c))
result = int(''.join(map(str, password)))
print(result)
# 73162890
