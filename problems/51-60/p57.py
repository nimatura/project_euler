from classes.numeric import RationalNumber


result = 0
base = RationalNumber(0)
for i in range(1000):
    base = (RationalNumber(1) / (RationalNumber(2) + base))
    approx = (RationalNumber(1) + base)
    if len(str(approx.p)) > len(str(approx.q)):
        result += 1

print(result)
# 153
