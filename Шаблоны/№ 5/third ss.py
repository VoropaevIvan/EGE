def ten_third(x):
    x_3 = ''
    while x != 0:
        x_3 = str(x % 3) + x_3
        x //= 3
    return x_3


def third_ten(x):
    x_10 = 0
    for i in range(1, len(str(x)) + 1):
        x_10 += int(str(x)[-i]) * 3 ** (i - 1)
    return x_10


min_R = 1000000000
for N in range(1, 10000):
    n_3 = ten_third(N)
    if N % 3 == 0:
        n_3 = n_3 + n_3[-2:]
    else:
        ost = N % 3 * 5
        n_3 = n_3 + ten_third(ost)
    r = third_ten(n_3)
    if r > 180:
        min_R = min(min_R, r)
print(min_R)
