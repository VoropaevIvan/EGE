def f(x1, x2, moves, win):
    if x1 + x2 >= 259:
        return moves in win
    if len(moves) > 4:
        return 0
    if moves == '' or moves[-1] == 'V':
        return f(x1+1, x2, moves+'P', win) or f(x1*2, x2, moves+'P', win) or f(x1, x2+1, moves+'P', win) or f(x1, x2*2, moves+'P', win) # Ход Пети
    else:
        return f(x1+1, x2, moves+'V', win) and f(x1*2, x2, moves+'V', win) and f(x1, x2+1, moves+'V', win) and f(x1, x2*2, moves+'V', win) # Ход Вани


for s in range(1, 241+1):
    if f(5, s, '', ['P']) == 0 and f(5, s, '', ['P', 'PVP']) == 1:
        print(s)