def solve(n=4):
    """
    this function simulates a sieve, which marks the composite numbers and
    saves its prime divisors as witnesses for its compositeness
    """
    D = {}
    q = 2
    ctr = 0
    while ctr < n:
        if q not in D:
            ctr = 0
            D[q+q]   = [q]
        else:
            if len(D[q]) >= n:
                ctr += 1
            else:
                ctr = 0
            for p in D[q]:
                D.setdefault(p+q,[]).append(p)
            del D[q]
        q += 1
    return q - n 

solve()
