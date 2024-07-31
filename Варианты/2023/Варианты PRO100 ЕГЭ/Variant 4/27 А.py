with open('27-A.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    a = [int(s) for s in file]

ans = -1
for i in range(N):
    for j in range(i+K, N):
        ans = max(ans, (j - i) + a[i] + a[j])
print(ans)