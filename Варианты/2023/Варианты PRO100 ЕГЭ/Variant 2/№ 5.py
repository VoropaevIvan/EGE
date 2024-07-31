def from_10(n, base):
    res = ''
    while n != 0:
        last = n % base
        res = res + str(last)
        n //= base
    return res[::-1]


for n in range(1, 10**5):
    n_3 = from_10(n, 3)
    n_3_b = n_3
    if n % 2 == 0:
        n_3 = '1' + n_3 + '00'
    else:
        sum_d = n_3.count('1') + 2*n_3.count('2')
        sum_d_3 = from_10(sum_d, 3)
        n_3 = n_3 + sum_d_3

    r = int(n_3, 3)
    if r > 168:
        print(n)
        break
    print(n, n_3_b, n_3, r)