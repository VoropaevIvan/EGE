def f(x, c, pob):
    if x >= 129:
        return c in pob
    if c >= max(pob):
        return 0
    moves = [f(x + 1, c + 1, pob), f(x * 2, c + 1, pob)]
    if c % 2 == max(pob) % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 12 + 1):
    if f(s,  0, [1, 3]) == 1:
        print('№ 19:', s)
    # if f(s,  0, [2]) == 0 and f(s,  0, [2, 4]) == 0:
    #     print('№ 20:', s)
    # if f(s,  0, [2, 4]) == 1 and f(s, 0, [2]) == 0:
    #     print('№ 21:', s)