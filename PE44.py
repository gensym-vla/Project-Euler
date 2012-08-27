from math import sqrt
def pents():
    pent, ct = 1, 1
    while True:
        yield pent
        ct += 1
        pent += 3*ct - 2

is_pentagonal = lambda n : n >= 1 and  ((sqrt(24 * n + 1) + 1)/6.).is_integer()

def solve():
    lst = []
    for p in pents():
        for q in lst[1:]:
            if is_pentagonal(p - q) and is_pentagonal(p + q):
                    print "Answer to PE44 is {0}".format(p - q)
                    return p - q
        lst.append(p)
solve()
