from itertools import combinations, permutations, imap
perms  = lambda x : imap(lambda z : "".join(z), permutations(x))
primes = [2,3,5,7,11,13, 17]

def find_sum(prefix):
    """
    sums up all 0 to 9 pandigital numbers, with the substring divisiblity
    property starting with the prefix, `prefix`
    """
    if len(prefix) == 10:
        return int(prefix)
    else:
        prime = primes[len(prefix) - 3]
        sum = 0
        for i in range(10):
            if str(i) in prefix:
                continue
            elif int(prefix[-2:] + str(i)) % prime == 0:
                sum += find_sum(prefix + str(i))
        return sum
def solve():
    # iterate over possible prefixes
    sum = 0
    digits = '1234567890'
    for c in combinations(digits, 3):
        for p in perms(c):
            if p[0] == '0':
                continue
            sum += find_sum(p)
    print "Answer to PE43: {0}".format(sum)

solve()
