'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
from prime import get_prime, is_prime

result, i = {}, 0
p = get_prime(i)

def get_next_number(x):
    return (x % 10) * (10 ** (len(str(x)) - 1)) + x / 10

while p < 1000000:
    if result.get(p, 0):
        continue;
    else:
        t = get_next_number(p)
        while t != p:
            if is_prime(t):
                t = get_next_number(t)
            else:
                break
        if t == p:
            result[p] = 1
    i += 1
    p = get_prime(i)

print len(result)
