def f(x, moves):
    if x >= 129:
        return moves == 'PVPV' or moves == 'PV'

    if moves == '' or moves[-1] == 'V':
        return f(x + 1, moves + 'P') and f(x * 2, moves + 'P')  # Ход Пети
    else:
        return f(x + 1, moves + 'V') or f(x * 2, moves + 'V')  # Ход Вани


for s in range(1, 128 + 1):
    if f(s, ''):
        print(s)

