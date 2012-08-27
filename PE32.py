from itertools import permutations, combinations, imap
from time import time

perms         = lambda x : imap(lambda z: "".join(z), permutations(x))
is_pandigital = lambda x : len(x) == 9 and all(z in x for z in map(str,range(1,10)))

def is_product(x):
    sprod = int(x)
    return any(sprod % i == 0 and is_pandigital(x + str(i) + str(sprod/i))
                for i in range(1, 100))

def solve():
    st = time()
    results = set()
    for c in combinations(map(str, range(1,10)),4):
        for p in perms(c):
            if int(p) in results:
                continue
            if is_product(p):
                results.add(int(p))
    s = sum(results)    
    print "Answer to PE32 is: {0}\nTime: {1}".format(s, time() - st)
    return s

solve()

