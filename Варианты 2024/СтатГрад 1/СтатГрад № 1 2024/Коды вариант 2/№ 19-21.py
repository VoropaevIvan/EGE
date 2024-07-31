def f(x, c, max_):
    if x >= 84:
        return c % 2 == max_ % 2
    if c == max_:
        return 0

    if x % 2 == 0:
        moves = [f(x + 1, c + 1, max_), f(x * 15 // 10, c + 1, max_)]
    else:
        moves = [f(x + 1, c + 1, max_), f(x * 2, c + 1, max_)]
    if c % 2 != max_ % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 83 + 1):
    for j in range(1, 100):
        if f(s, 0, j) == True:
            if j == 2:
                print('№ 19', s)
            if j == 3:
                print('№ 20', s)
            if j == 4:
                print('№ 21', s)
            break

# 70
# 27 29
# 52