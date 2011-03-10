if __name__ == "__main__":
    ll = 0
    l = 1
    current = ll + l
    sum = 0
    while current < 4000000:
        if current%2 == 0:
            sum += current
        ll = l
        l = current
        current = ll + l

    print sum
