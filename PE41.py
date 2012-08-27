"""
No 9 digit pandigital number can be a prime 1 + ... + 9 = 45 -> divisible by 9
No 8 digit pandigital number cab be a prime ! + ... + 8 = 36 -> divisible by 9
We compute all the primes up to 10^7, and find the greatest pandigital
"""
from itertools import permutations, imap
from time import time
from math import sqrt 

perms = lambda x : imap(lambda z : int("".join(z)), permutations(x))
pand = lambda x : len(x) <= 9 and all(z in x  for z in map(str, range(1, len(x) + 1)))
isPrime = lambda x : x % 2 != 0 and all(x % z != 0
                                        for z in range(3, int(sqrt(x + 1)), 2))
possible = lambda x : sum(range(1,x + 1)) % 3 != 0
def solve():
    st = time()
    try:
        for i in filter(possible, range(7, 0, -1)):
            for p in perms(map(str, range(i,0, -1))):
                if isPrime(p):
                    raise Exception,p
    except Exception, p:
        print "Answer to PE41 is {0}.\nTime: {1}".format(p, time() - st)

solve()
