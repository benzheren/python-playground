'''
215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
'''

def sum_of_digits(n):
    sum = 0;
    while n > 0:
        sum += (n % 10)
        n /= 10
    return sum

print sum_of_digits(2 ** 1000)
