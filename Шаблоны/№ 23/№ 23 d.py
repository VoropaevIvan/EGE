def f(start, end):
    d = [0] * 1000
    d[start] = 1
    for i in range(start, end):
        d[i + 1] += d[i]
        d[i * 2] += d[i]
        d[18] = 0
    return d[end]


print(f(1, 10) * f(10, 21))
