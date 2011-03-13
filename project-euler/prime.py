primes = [2, 3, 5, 7, 11, 13]
primes_dict = dict.fromkeys(primes, 1)
lastn = primes[-1]

def _is_prime(n):
    for prime in primes:
        if prime * prime > n: break
        if not n % prime: return False
    primes_dict[n] = 1
    return True

def _refresh(x):
    global lastn
    while lastn <= x:
        lastn = lastn + 2
        if _is_prime(lastn):
            primes.append(lastn)

def get_prime(n):
    """get nth prime"""
    global lastn
    while len(primes) <= n:
        lastn = lastn + 2
        while not _is_prime(lastn):
            lastn += 2
        primes.append(lastn)

    return primes[n]

def is_prime(x):
    _refresh(x)
    return primes_dict.get(x, 0)
