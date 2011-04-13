import sys
from string import atoi

n = atoi(sys.stdin.readline())

for i in xrange(1, n+1):
    if not i % 15:
        print 'Hop'
    elif not i % 3:
        print 'Hoppity'
    elif not i % 5:
        print 'Hophop'

