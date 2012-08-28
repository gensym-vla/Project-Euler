from utils.sieve import is_prime

def diag_num():
    """
    returns the diagonal values at the (i+1)-st iteration,
    as the last value is always a square, we don't include it in the output
    """
    val  = [1,1,1]
    incr = [2,4,6]
    while True:
        for i in range(3):
            val[i] += incr[i]
            incr[i] += 8
        yield val

def solve(r=0.1):
    diag_count  = 1 # 1 sits in the center of the spiral
    prime_count = 0 # 1 is not a prime 
    for i,v in enumerate(diag_num()):
        diag_count  += 4
        prime_count += sum(map(is_prime, v))
        if prime_count*1./diag_count < r:
            # see remark on diag_num
            print "Answer to PE54 is: {0}".format(2*(i + 1) + 1)
            return 2*(i+1) - 1

solve()
