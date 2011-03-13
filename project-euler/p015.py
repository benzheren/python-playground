'''
Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

How many routes are there through a 20x20 grid?

'''
def route(max):
    result = [[0] * (max+1) for x in xrange(max+1)]
    result[0][0] = 1
    for i in range(max+1):
        for j in range(max+1):
            if i >= 1:
                result[i][j] += result[i-1][j]
            if j >= 1:
                result[i][j] += result[i][j-1]
    return result[max][max]

print route(20)
