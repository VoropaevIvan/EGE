def f(x1, x2, c, pob):
    if x1**2 + x2**2 >= 13**2:
        return c in pob
    if c >= max(pob):
        return 0
    moves = [f(x1 + 3, x2, c + 1, pob), f(x1, x2 + 3, c + 1, pob), f(x1, x2 + 4, c + 1, pob)]
    if c % 2 != max(pob) % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 12 + 1):
    if f(s, 2, 0, [2]) == 1:
        print('№ 19:', s)
    if f(s, 2, 0, [3]) == 1:
        print('№ 20:', s)
    if f(s, 2, 0, [2, 4]) == 1 and f(s, 2, 0, [2]) == 0:
        print('№ 21:', s)



# П В П В
# 1 2 3 4
