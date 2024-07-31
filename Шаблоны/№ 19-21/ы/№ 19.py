def f(x, game):
    if x >= 129:
        return game == 'PVP'

    if game[-1] == 'P':
        return f(x + 1, game + 'V') and f(x * 2, game + 'V')
    else:
        return f(x + 1, game + 'P') or f(x * 2, game + 'P')


for s in range(1, 128 + 1):
    if f(s, 'P'):
        print(s)