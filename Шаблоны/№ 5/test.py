min_r = 100000000
for n in range(1, 10000):
    n_2 = bin(n)[2:]
    n_2 = n_2.replace('1', '*')
    n_2 = n_2.replace('0', '01')
    n_2 = n_2.replace('*', '10')

    r = int(n_2, 2)
    if r > 63:
        if r < min_r:
            min_r = r
print(min_r)