d = [0]*10_000
for n in range(0, 3):
    d[n] = n
for n in range(3, 2024+1):
    if n % 2 == 0:
        d[n] = 2*(n-1) + d[n-1] + 2
    else:
        d[n] = 2 * (n + 1) + d[n - 2] - 5

print(d[32])