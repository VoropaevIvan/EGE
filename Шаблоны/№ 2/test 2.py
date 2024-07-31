from itertools import *

columns = 'xyzw'
def F(x, y, z, w):
    return not (y <= x) or (z <= w) or (not z)

for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    table = [
        (x1, 0, x2, x3) + (0,),
        (0, 1, x4, x5) + (0,),
        (1, x6, x7, 0) + (0,)
    ]

    if len(table) == len(set(table)):
        for p in permutations([0, 1, 2, 3]):
            if all( F(s[p[0]], s[p[1]], s[p[2]], s[p[3]]) == s[-1] for s in table):
                print(*p, sep='')
