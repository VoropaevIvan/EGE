def f(x, c, max_):
    if x >= 129:
        return c % 2 == max_ % 2
    if c == max_:
        return 0

    if c % 2 != max_ % 2:
        return f(x + 1, c + 1, max_) or f(x * 2, c + 1, max_)
    else:
        return f(x + 1, c + 1, max_) and f(x * 2, c + 1, max_)


for s in range(1, 128 + 1):
    for j in range(1, 100):
        if f(s, 0, j) == True:
            if j % 2 == 0:
                print(s, j)
            break
