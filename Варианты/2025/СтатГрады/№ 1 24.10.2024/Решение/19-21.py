def f(x, c, win):
    if x <= 19:
        return c in win
    if c == max(win):
        return 0
    moves = [f(x - 1, c + 1, win)]
    if x % 3 == 0:
        moves.append(f(x // 3, c + 1, win))
    else:
        moves.append(f(x - 2, c + 1, win))
    if x % 5 == 0:
        moves.append(f(x // 5, c + 1, win))
    else:
        moves.append(f(x - 3, c + 1, win))
    if c % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)

for s in range(20, 1000):
    if f(s, 0, [2]) == 0 and f(s, 0, [2, 4]) == 1:
        print(s)