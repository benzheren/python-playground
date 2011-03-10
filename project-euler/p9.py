'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
def get(n):
    for c in xrange(n/3+1, n):
        for b in xrange(n-c-1, c/2, -1):
            a = n - c - b
            diff = c * c - a * a - b * b
            if not diff:
                return a * b * c
            elif diff > 0:
                break

print get(1000)
