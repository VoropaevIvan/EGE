
i = 1
def f(d):
    global i
    d[0] = i
    i += 1
    print(d)
    f(d)
f({})


