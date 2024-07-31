def f(x, end):
    if x > end or x in [11, 12]:
        return 0
    if x == end:
        return 1
    return f(x+1, end) + f(x*2, end) + f(x*x, end)

print(f(2, 10) * f(10, 40))