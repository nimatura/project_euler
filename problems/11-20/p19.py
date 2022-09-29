"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

from itertools import cycle
from functions.text import days_by_month


months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
          'november', 'december']
days_of_week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

months_cycle = cycle(months)
days_of_week_cycle = cycle(days_of_week)

current_year = 1900
current_month = next(months_cycle)
current_day_of_month = 1

result = 0
for current_day_of_week in days_of_week_cycle:
    if current_day_of_week == 'sunday' and current_day_of_month == 1 and current_year >= 1901:
        print('%s-%s-%s : %s' % (current_year, current_month, current_day_of_month, current_day_of_week))
        result += 1
    if current_day_of_month == days_by_month(current_month, current_year):
        if current_month == 'december':
            current_year += 1
        current_day_of_month = 1
        current_month = next(months_cycle)
    else:
        current_day_of_month += 1
    if current_year > 2000:
        break
print(result)
# 171
