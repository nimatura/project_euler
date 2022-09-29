def number_to_words(n):
    base_words = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety'
    }
    if n in base_words.keys():
        return base_words[n]
    if 20 <= n <= 9999:
        aux1 = n % 10
        aux2 = n % 100
        aux3 = n % 1000
        aux4 = n % 10000
        d1 = aux1
        d2 = int((aux2 - aux1) / 10)
        d3 = int((aux3 - aux2) / 100)
        d4 = int((aux4 - aux3) / 1000)
        result = ''
        if d4 > 0:
            result += '%s thousand ' % base_words[d4]
        if d3 > 0:
            result += '%s hundred ' % base_words[d3]
        if aux2 > 20:
            if d2 > 0:
                if len(result) > 0:
                    result += 'and '
                result += '%s' % base_words[10 * d2]
            if d1 > 0:
                result += '-%s' % base_words[d1]
        elif aux2 > 0:
            result += 'and %s' % base_words[aux2]
        result = result.strip()
        return result


def days_by_month(month, year=None):
    regular_days = {
        'january': 31,
        'february': 28,
        'march': 31,
        'april': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'august': 31,
        'september': 30,
        'october': 31,
        'november': 30,
        'december': 31
    }
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december']

    if ((type(month) == str and month.lower() == 'february') or (type(month) == int and month == 2)) and \
            year is not None and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 29
    elif type(month) == int and 1 <= month <= 12:
        return regular_days[months[month + 1]]
    elif type(month) == str and month.lower() in regular_days.keys():
        return regular_days[month.lower()]
    else:
        print('invalid month')


def alphabetical_value(word: str):
    offset = ord('a') - 1
    result = 0
    for char in word.lower():
        char_value = ord(char) - offset
        result += char_value
    return result


def is_palindrome(string):
    half_length = int(len(string) / 2)
    for i in range(half_length):
        if string[i] != string[-(i + 1)]:
            return False
    return True


def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
