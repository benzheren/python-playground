'''
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
'''
days_in_a_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

start = 366 # jan 1st 1901 is 366
num = 0;
for i in xrange(1901, 2001):
    for j in xrange(12):
        if j == 1 and not i % 4:
            start += (days_in_a_month[j] + 1)
        else:
            start += days_in_a_month[j]
        if not start % 7: num += 1

print num
