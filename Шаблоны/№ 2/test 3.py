from itertools import *
columns = 'xyzw'

for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    table = [
        (x1,   0,   x2,  x3),
        (0,    1,   x4,  x5),
        (1,    x6,  x7,  0)
    ]
    ok_ans = [0, 0, 0]
    if len(table) == len(set(table)):
        for p in permutations([0, 1, 2, 3]):
            ans = []
            for s in table:
                x, y, z, w = s[p[0]], s[p[1]], s[p[2]], s[p[3]]
                F = not (y <= x) or (z <= w) or (not z)
                ans.append(F)
            if ans == ok_ans:
                for i in p:
                    print(columns[i], end='')
