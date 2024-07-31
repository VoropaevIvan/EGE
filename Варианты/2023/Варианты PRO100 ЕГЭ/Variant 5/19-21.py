def f(x, moves, win):
    if x >= 21:
        return moves in win
    if moves == '' or moves[-1] == 'V':
        return f(x+1, moves+'P', win) or f(x*2, moves+'P', win)
    else:
        return f(x+1, moves + 'V', win) and f(x*2, moves + 'V', win)

for s in range(1, 20+1):
    if f(s, '', ['P']) == 0 and f(s, '', ['P', 'PVP']) == 0 and f(s, '', ['P', 'PVP', 'PVPVP']) == 1:
        print(s)
