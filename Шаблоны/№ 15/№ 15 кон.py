def check(A):
    for x in range(0, 10 ** 6):
        f = ((x&42 != 0) and (x&34 == 0)) <= (not x&A == 0)
        if f != 1:
            return 0
    return 1


for A in range(1, 1000):
    if check(A) == 1:
        print(A)
        break
