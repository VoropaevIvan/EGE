d = [0]*10_000
d[1] = 3
for n in range(2, 2024+1):
    d[n] = 3*n + 2*d[n-1]
print(d[2024] - 4*d[2022])