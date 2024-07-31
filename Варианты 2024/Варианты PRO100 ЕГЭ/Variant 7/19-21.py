def f(x1, x2, x3, c, pob):
    if (x1 + x2 + x3 >= 25) or max(x1, x3, x3) >= 20:
        return c in pob
    if c >= max(pob):
        return 0
    moves = [f(x1*2, x2, x3, c + 1, pob),
             f(x1, x2*2, x3, c + 1, pob),
             f(x1, x2, x3*2, c + 1, pob),
             f(x1 + 2, x2 + 2, x3 + 2, c + 1, pob)]
    if c % 2 != max(pob) % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 19 + 1):
    if f(2, 3, s, 0, [1]) == 0 and f(2, 3, s, 0, [2]) == 1:
        print('№ 19:', s)


# П В П В
# 1 2 3 4
