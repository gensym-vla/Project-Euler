from math import sqrt
from functools import reduce

alphabet = map(chr, range(65, 65 + 26))
vals     = dict(zip(alphabet, range(1, 27)))

def is_triangular(word):
    num_val = sum(vals[c] for c in word)
    m       = sqrt(2*num_val)
    if int(m) * int(m + 1) == 2 * num_val:
        return True
    else:
        return False

def solve(fd = "files/pe42_words.txt"):
    with open(fd,"r") as f:
        a = map(lambda z: z[1:-1], f.read().split(','))
    r = reduce(lambda x, w: x + 1 if is_triangular(w) else x, a, 0)
    print "Answer to PE42: {0}".format(r)
    return r

solve()
