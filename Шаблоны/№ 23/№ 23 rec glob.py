def f(x, end):
    global otv
    if x == 18:
        return
    if x == end:
        otv += 1
    if x > end:
        return
    f(x + 1, end)
    f(x * 2, end)


otv = 0
f(1, 10)
f(10, 21)
print(otv)
