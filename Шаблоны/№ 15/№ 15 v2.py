# А наибольший
A = 1
f_usl = 1

for x in [k/4 for k in range(-10_000, 10_000)]:
    P = 9 <= x <= 19
    Q = 24 <= x <= 54
    f = (A) <= (Q or P)
    if f == f_usl:
        print(x)




