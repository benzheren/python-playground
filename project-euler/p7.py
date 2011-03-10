'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

'''
primes = [2, 3, 5, 7, 11, 13]

def _is_prime(n):
    for prime in primes:
        if prime * prime > n: break
        if not n % prime: return False

    return True

def _get_prime(n):
    """get nth prime"""
    while len(primes) < n:
        last = primes[-1] + 2
        while not _is_prime(last):
            last += 2
        primes.append(last)

    return primes[-1]

print   _get_prime(10001)
