sum = 0

for i in xrange(1, 1000):
    if not i%3 or not i%5:
        sum += i

print sum
