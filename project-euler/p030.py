'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

'''
def sum_of_digits(n, p):
    sum = 0
    while n > 0:
        sum += (n % 10) ** p
        n /= 10
    return sum

print sum(n for n in xrange(2, 200000) if sum_of_digits(n, 5) == n)
