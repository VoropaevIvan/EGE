otv_N = -1
max_R = -1
for N in range(1, 10000):
    n_2 = bin(N)[2:]
    if N % 2 == 0:
        n_2 = '1' + n_2 + '00'
    else:
        sum_d = n_2.count('1')
        n_2 = n_2 + bin(sum_d)[2:]
    r = int(n_2, 2)
    if r <= 68:
        if r > max_R:
            max_R = r
            otv_N = N
            print(r, N)
print(otv_N)