from utils.sieve import unbded_sieve
import time
def solve():
    st = time.time()
    primes = set()
    trunctables = []
    isTrunctable = lambda x : len(x) > 1 and all(x[:z] in primes and  x[z:] in primes
                                                        for z in range(1, len(x)))
    for p in unbded_sieve():
        primes.add(str(p))
        if isTrunctable(str(p)):
            trunctables.append(p)
            if len(trunctables) >= 11:
                break
    s = sum(trunctables)
    print ("Answer to PE37 is {0}\nThe trunctable primes are: "+
            "{1}\nTime: {2}").format(s, trunctables, time.time() - st)
    return s

solve()
