def check(A):
    for x in range(1000):
        for y in range(1000):
            f = (3*x + y > 48) or (x > y) or (4*x + y < A)
            if f == 0:
                return 1
    return 0


for A in range(1, 10000):
    if check(A):
        print(A)
