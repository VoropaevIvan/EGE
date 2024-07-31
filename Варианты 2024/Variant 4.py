def from_10(n, base):
    res = ''
    while n != 0:
        last = n % base
        res = res + str(last)
        n //= base
    return res[::-1]


for n in range(1, 10**5):
    n_4 = from_10(n, 4)
    count_d = len(n_4)
    if count_d % 2 == 0:
        n_4 = n_4[:count_d//2] + '0' + n_4[count_d//2:]

    r = int(n_4)
    if r <= 180:
        print(n)
