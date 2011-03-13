def max(triangle):
    for i in xrange(len(triangle) - 2, -1, -1):
        for j in xrange(0, i+1):
            triangle[i][j] = int(triangle[i][j]) + \
                            (int(triangle[i+1][j]) > int(triangle[i+1][j+1]) and
                             int(triangle[i+1][j]) or int(triangle[i+1][j+1]))

    print triangle[0][0]

triangle = []
f = open('067.txt', 'r')
for line in f:
    triangle.append(line.split())

max(triangle)

