'''
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91*99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
from time import time
start = time()
n = 0
for i in xrange(999, 100, -1):
    if i * i < n:
        break

    for j in xrange(i, n/i >=100 and n/i or 100, -1):
        x = i * j
        s = str(x)
        if s == s[::-1] and x > n:
            n = x

end = time()

print n
print end - start
