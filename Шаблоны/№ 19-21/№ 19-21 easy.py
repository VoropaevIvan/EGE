def f(s, k, win):
    if s >= 443:
        return k in win
    if k == max(win):
        return 0
    moves = [f(s + 1, k + 1, win), f(s + 3, k + 1, win), f(s * 2, k + 1, win)]
    if k % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)


for s in range(1, 442 + 1):
    if f(s, 0, [2]) == 1:
        print(s)
