'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.
'''
fact = (1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)

def is_curious_number(n):
    sum = 0;
    while n > 0:
        sum += fact[n % 10]
        n /= 10
    return sum

print sum(x for x in xrange(3, 100000) if x == is_curious_number(x))
