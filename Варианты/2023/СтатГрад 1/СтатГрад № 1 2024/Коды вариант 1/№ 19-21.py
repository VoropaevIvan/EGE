def f(s, k, win):
    if s >= 108:
        return k in win
    if k == max(win):
        return 0

    if s % 2 == 0:
        moves = [f(s + 1, k + 1, win), f(int(s*1.5), k + 1, win)]
    else:
        moves = [f(s + 1, k + 1, win), f(s * 2, k + 1, win)]

    if k % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 107 + 1):
    if f(s, 0, []) == 1:
        print(s)
