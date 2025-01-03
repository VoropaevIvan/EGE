def f(s, k, win):
    if s >= 108:
        return k in win
    if k == max(win):
        return 0

    if s % 2 == 0:
        moves = [f(s + 1, k + 1, win), f(s*15//10, k + 1, win)]
    else:
        moves = [f(s + 1, k + 1, win), f(s * 2, k + 1, win)]

    if k % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 107 + 1):
    if (f(s, 0, [2, 4]) == 1) and (f(s, 0, [2]) == 0):
        print(s)

# П В П В