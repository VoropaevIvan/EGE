from itertools import *

def F(x, y, z, w):
    return ((x <= z) <= y) or (not w)

for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    table = [
        (1, 0, x1, x2) + (0,),
        (x3, 1, 0, x4) + (0,),
        (0, x5, x6, x7) + (0,)
    ]

    if len(table) == len(set(table)):
        for p in permutations('xyzw'):
            if all(F(**dict(zip(p, s))) == s[-1] for s in table):
                print(*p, sep='')
