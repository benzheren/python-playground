import sys
from string import atoi

def read_input(file):
    n = atoi(file.readline())
    def read_activity(s):
        return (s.split()[0], atoi(s.split()[1]))
    return map(lambda x: read_activity(file.readline()), xrange(n)) 

def solve(activities):
    pos = sum(x[1] for x in activities if x[1] > 0 )
    neg = sum(x[1] for x in activities if x[1] < 0 )
    sol = [map(lambda x: activities[0][1] == x + neg, xrange(pos - neg + 1))]
    for i in xrange(1, len(activities)):
        temp = [False] * (pos - neg + 1)
        for j in xrange(pos - neg + 1):
            temp[j] = ((j - activities[i][1]) >= 0 and (j - activities[i][1]) < pos - neg
             + 1) and (sol[i-1][j] or (activities[i][1] == j + neg) or\
                    sol[i - 1][j - activities[i][1]]) or (activities[i][1] == 
                                                         j + neg)
            if temp[j] and j == -neg:
                break
        if temp[-neg]:
            break
        sol.append(temp)

    results = []
    if len(sol) >= len(activities):
        print 'no solution'
    else:
        i, j = len(sol), -neg
        while i >= 1:
            if sol[i-1][j]:
                i -= 1
            elif activities[i][1] == j + neg:
                results.append(activities[i][0])
                break
            elif 0 <= j - activities[i][1] < pos - neg + 1 and \
                    sol[i-1][j - activities[i][1]]:
                results.append(activities[i][0])
                j -= activities[i][1]
                i -= 1
        if activities[0][1] == j:
            results.append(activities[0][0])
        
        results.sort()
        for r in results:
            print r


if __name__ == "__main__":
    solve(read_input(sys.stdin))
