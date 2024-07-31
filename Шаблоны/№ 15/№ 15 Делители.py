def check(A):
    for x in range(0, 10 ** 6):
        x_a = (x % A == 0)
        x_12 = (x % 12 == 0)
        x_14 = (x % 14 == 0)
        f = (not x_a) <= (x_12 <= (not x_14))
        if f != 1:
            return 0
    return 1


for A in range(1, 10000):
    if check(A) == 1:
        print(A)
