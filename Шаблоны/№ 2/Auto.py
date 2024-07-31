from itertools import *

def F(x, y, z, w):
    return not (y <= x) or (z <= w) or (not z)

for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    table = [
        (x1, 0, x2, x3) + (0,),
        (0, 1, x4, x5) + (0,),
        (1, x6, x7, 0) + (0,)
    ]

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(F(**dict(zip(p, s))) == s[-1] for s in table):
                print(*p, sep='')
