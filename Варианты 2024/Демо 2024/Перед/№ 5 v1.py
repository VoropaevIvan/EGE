min_r = 1000000
for n in range(1, 10**5):
    n_2 = bin(n)[2:]

    if n % 3 == 0:
        n_2 = n_2 + n_2[-3:]
    else:
        ost = (n % 3) * 3
        ost_2 = bin(ost)[2:]
        n_2 = n_2 + ost_2

    r = int(n_2, 2)
    if r > 151:
        if r < min_r:
            min_r = r
print(min_r)