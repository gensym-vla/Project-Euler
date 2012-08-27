from math import sqrt
from itertools import count

def eratosthenes(n):
    """
    sieve of eratosthenes
    """
    isPrime = [False, True] * ((n+1) / 2)
    isPrime[0] = True
    lim     = int(sqrt(n+1))
    for i in range(1,lim+1):
        if isPrime[i]:
            for j in range((i+2)**2 - 2, n, 2*i + 4):
                isPrime[j] = False
    return filter(lambda x: isPrime[x - 2], range(2, n+1))

def unbded_sieve():
    """
    an unbounded version of the sieve of eratosthenes, a generator of infinite
    primes
    taken from: http://macdevcenter.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html?page=2
    """
    D = {}
    yield 2
    for q in count(3,2):
        p = D.pop(q, None)
        if p is None:
            D[q * q] = 2 * q
            yield q
        else:
            x = p + q
            while x in D:
                x += p
            D[x] = p
