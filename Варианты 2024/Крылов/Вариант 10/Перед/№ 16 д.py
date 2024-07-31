d = [0]*10_000
d[1] = 1
for n in range(2, 2023+1):
    d[n] = n**2 + d[n-1]
print(d[2023] - d[2019])