k = 1024*768
N = 4096
i = 12
v = 128 * 1024 * 8
for pr in range(1, 99+1):
    I = k*i*100 * (100-pr)/100
    if I / v <= 6*60:
        print(pr)
