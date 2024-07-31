def f(x, c):
    if x >= 30:
        return c == 3
    if c == 3:
        return 0

    return f(x + 1, c + 1) or f(x * 2, c + 1)


for s in range(1, 29 + 1):
    if f(s, 0):
        print(s)

# Е П В
