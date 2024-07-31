def f(x, moves):
    if x >= 129:
        return moves in ['PVPV', 'PV']
    if moves[-1:] == 'P': # Ход Вани
        return f(x+1, moves + 'V') and f(x*2, moves + 'V')
    else:
        return f(x+1, moves + 'P') or f(x * 2, moves + 'P')

for s in range(1, 128+1):
    if f(s, ''):
        print(s)


# За один ход: 64 127