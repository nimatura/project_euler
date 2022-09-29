"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


def multiply_list_by_two(list_number):
    result = []
    extra = 0
    for i, digit in enumerate(list_number[::-1]):
        digit_product = extra + 2 * digit
        result_digit = int(str(digit_product)[-1])
        extra = 0 if digit_product < 10 else int(str(digit_product)[:-1])
        if i < len(list_number) - 1:
            result.append(result_digit)
        else:
            for d in str(digit_product)[::-1]:
                result.append(int(d))
    return result[::-1]


power = 1000
product = [1]
for i in range(power):
    product = multiply_list_by_two(product)
print(sum(product))
# 1366
