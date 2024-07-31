A = 1
f_usl = 1
for x in range(-10_000, 10_000):
    P = x in {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
    Q = x in {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
    f = ((A) <= (P)) and ((not Q) <= (not A))
    if f == f_usl:
        print(x)
