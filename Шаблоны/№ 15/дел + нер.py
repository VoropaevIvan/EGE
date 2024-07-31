def check(A):
    for x in range(1, 10 ** 6):
        x_6 = (x % 6 == 0)
        x_10 = (x % 10 == 0)
        f = (x_6 <= (not x_10)) or (x + A > 121)
        if f != 1:
            return 0
    return 1


for A in range(1, 10000):
    if check(A) == 1:
        print(A)
