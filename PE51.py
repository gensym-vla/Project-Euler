from utils.sieve import eratosthenes
from itertools   import combinations
# generates an index list from [0...x-1] of the size y
indices = lambda x, y: combinations(map(str, range(x)), y)

# generate the family from a template
def get_fam(temp):
    rs  = set()
    for i in range(0 if temp[0] != '*' else 1, 10):
        rs.add(int(temp.replace('*', str(i))))
    return rs

primes   = set(eratosthenes(10**6))

def solve():
    # generate templates (the last digit should always be odd)
    for t in range(101,1000, 2):
        for c in indices(5,2):
            a = ['*']*6
            i, j = map(int,c)
            # last digit cannot be a `*`, or at least 4 number wd be composite
            a[i], a[j], a[5] = list(str(t))
            # assemble string
            temp = "".join(a)
            fam = get_fam(temp)
            if len(fam.intersection(primes)) >= 8:
                print fam.intersection(primes)
                print "Answer to PE51 is {0}".format(min(fam.intersection(primes)))
                return min(fam.intersection(primes))
solve()
