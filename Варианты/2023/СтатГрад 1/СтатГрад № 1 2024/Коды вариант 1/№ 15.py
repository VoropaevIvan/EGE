def check(A):
    for x in range(1000):
        for y in range(1000):
            f = (x + 2*y > 48) or (y > x) or (x + 3*y < A)
            if f == 0:
                return 1
    return 0


for A in range(1, 10000):
    if check(A):
        print(A)
