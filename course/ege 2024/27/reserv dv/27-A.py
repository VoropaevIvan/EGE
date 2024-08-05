with open('reservdv-A.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
ans = -1
for i in range(N):
    for j in range(i+1, N):
        for k in range(j + 2, N):
            for m in range(k + 1, N):
                ans = max(ans, (a[j]-a[i]) + (a[m]-a[k]))
print(ans)
