from utils.sieve import eratosthenes
from itertools   import permutations, imap, combinations


perms  = lambda x : imap(lambda z : int("".join(z)), permutations(str(x))) 

# this generates possible indices for the arithmetic sequence
indices = lambda x,y : combinations(map(str, range(x)), y)

def solve():
    encountered = set()
    primes      = eratosthenes(10**4)
    relevant    = set(filter(lambda x : x > 10**3, primes))
    ctr = 0
    for p in relevant:
        # skip primes that you already have dealt with
        if p in encountered:
            continue
        seq = set()
        for q in perms(p):
            if q in relevant:
                encountered.add(q)
                seq.add(q)
        # don't bother if less then 3 perms of p are primes
        if len(seq) >= 3:
            seq = sorted(seq)
            for sols in indices(len(seq), 3):
                i,j,k = map(int, sols)
                if seq[k] - seq[j] == seq[j] - seq[i]:
                    print (seq[i], seq[j], seq[k])
                    ctr += 1
                    if ctr == 2:
                        return
solve()

