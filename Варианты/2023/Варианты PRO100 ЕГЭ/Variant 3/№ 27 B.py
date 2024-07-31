with open('27-B.txt') as file:
    N, T, K = [int(x) for x in file.readline().split()]
    a = [[int(x) for x in s.split()] for s in file]

min_buy = 10**10
ans = -1

for i in range(T, N):
    min_buy = min(min_buy, a[i - T][0])
    count = K // min_buy
    virochka = count * a[i][1]
    ans = max(ans, virochka - count*min_buy)
print(ans)


