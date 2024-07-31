with open('27-T.txt') as file:
    N, T, K = [int(x) for x in file.readline().split()]
    a = [[int(x) for x in s.split()] for s in file]

ans = -1
for i in range(N):
    for j in range(i + T, N):
        count = K // a[i][0]
        virochka = count * a[j][1]
        ans = max(ans, virochka - count*a[i][0])
print(ans)
