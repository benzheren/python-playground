'''
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''
results_dict = {1: 1}

def path_length(n):
    if n in results_dict:
        return results_dict[n]
    elif not n % 2:
        l = path_length(n/2) + 1
        results_dict[n] = l
        return l
    else:
        l = path_length(n * 3 + 1) + 1
        results_dict[n] = l
        return l

num, n = 0, 0
for x in xrange(1, 1000000):
    l = path_length(x)
    if l > num:
        num, n = l, x

print n
