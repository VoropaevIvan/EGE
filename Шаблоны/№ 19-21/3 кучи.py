def f(x, c, pob):
    if x >= 73:
        return c in pob
    if c > max(pob):
        return 0
    moves = [f(x + 3, c + 1, pob), f(x + 13, c + 1, pob), f(x + 23, c + 1, pob)]
    if c % 2 != max(pob) % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 442 + 1):
    if f(2 + 3 * s, 0, [2]) == 1:
        print('№ 19:', s)
    # if f(2 + 3 * s, 0, [3]) == 1:
    #     print('№ 20:', s)
    # if f(2 + 3 * s, 0, [2, 4]) == 1 and f(2 + 3 * s, 0, [2]) == 0:
    #     print('№ 21:', s)
