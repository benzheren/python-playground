def sum(max):
    sum = 0
    for i in range(1, max):
        if i%3 == 0 or i%5 == 0:
            sum += i
    return sum

if __name__ == "__main__":
    print sum(1000)
