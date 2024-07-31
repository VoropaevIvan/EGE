def f(x, moves, win):
    if x >= 129:
        return moves in win
    if moves == '' or moves[-1] == 'V':
        return f(x+1, moves+'P', win) or f(x*2, moves+'P', win) # Ход Пети
    else:
        return f(x+1, moves+'V', win) and f(x*2, moves+'V', win) # Ход Вани


for s in range(1, 128+1):
    if f(s, '', ['P']) == 0 and f(s, '', ['P', 'PVP']) == 1:
        print(s)