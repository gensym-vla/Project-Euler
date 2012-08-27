from utils.sieve import eratosthenes
import time
def rots(n):
    org = str(n)
    val = str(n)
    while True:
        val = val[-1:] + val[:-1] 
        yield int(val)
        if val == org: break

def solve(n=10**6):
    # get a list of the primes below n
    start = time.time()
    primes = eratosthenes(n)
    primest = time.time()
    # every prime contianing an even digit with the exception of 2 is not
    # circular
    mark = lambda x : x == 2 or all(c not in str(x) for c in map(str, [0,2,4,6,8]))
    # mark all potentially safe primes
    sprimes = filter(mark, primes)
    markt = time.time()
    circs = {}
    count = 0
    for p in sprimes:
        if p not in circs:
            val = all(x in sprimes for x in rots(p))
            for x in rots(p):
                circs[x] = val
        if circs[p]:
            count += 1
    end = time.time()
    print ("Solution to PE35: {0}.\nSieve populated in {1}.\nUnsafe primes" +
            " filtered in {2}.\nCircular primes found in {3}.\nTot" +
            " time: {4}.").format(count, primest - start, markt - primest, end - markt,
                                 end - start)
solve()
