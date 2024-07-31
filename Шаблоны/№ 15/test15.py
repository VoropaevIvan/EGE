A = 1
f_usl = 1
for x in [k * 0.25 for k in range(-10_000, 10_000)]:
    P = 10 <= x <= 23
    Q = 39 <= x <= 55
    f = ((not P) and A) <= ((Q and A) and A)
    if f == f_usl:
        print(x)