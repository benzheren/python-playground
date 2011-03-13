f = open('names.txt', 'r')
names = f.readline().split(',')
names. sort()
total = 0
for i in xrange(len(names)):
    sum = 0
    for j in names[i]:
        if not j == '"':
            sum += ((ord(j) - ord('A')) + 1)
    total += (sum * (i + 1))

print total
