def to_ten(x, base):
    x_10 = 0
    for i in range(len(x)):
        x_10 += x[-i - 1] * base ** i
    return x_10


def to_ten_1(x, base):
    return sum(x[-i - 1] * base ** i for i in range(len(x)))


for x in range(15):
    a = to_ten_1([9, 7, 9, 6, 8, x, 1, 5], 15)
    b = to_ten_1([7, x, 2, 3, 3], 15)
    if (a + b) % 14 == 0:
        print((a + b) // 14)
