def check(A):
    for x in range(0, 10**4):
        for y in range(0, 10**3):
            f = (x + 2*y < A) or (y > x) or (x > 60)
            if f != 1:
                return 0
    return 1


for A in range(0, 1000):
    if check(A) == 1:
        print(A)
        break
