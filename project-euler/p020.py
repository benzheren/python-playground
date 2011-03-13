'''
Find the sum of the digits in the number 100!
'''
import math

def sum_of_digits(n):
    sum = 0;
    while n > 0:
        sum += n % 10
        n /= 10
    return sum

print sum_of_digits(math.factorial(100))
