def check(A):
    for x in range(0, 10 ** 6):
        x_A = (x % A == 0)
        x_12 = (x % 12 == 0)
        x_B = 70 <= x <= 80
        f = x_12 and x_B and (not x_A)
        if f != 0:  # Подставляем значение функции из условия
            return 0
    return 1


for A in range(1, 1000):
    if check(A) == 1:
        print(A)

