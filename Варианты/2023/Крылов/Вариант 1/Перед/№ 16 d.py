d = [0]*10_000
d[1] = 5
for n in range(2, 2024+1):
    d[n] = 2*n + 1 + d[n-1]
print(d[2024] - d[2022])