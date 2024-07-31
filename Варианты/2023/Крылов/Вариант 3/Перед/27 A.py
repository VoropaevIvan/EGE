with open('27v03_A.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    a = [int(s) for s in file]

ans = 10**10
for i1 in range(N):
    for i2 in range(i1+K, N):
        for i3 in range(i2+K, N):
            ans = min(ans, a[i1] * a[i2] * a[i3])
print(ans)