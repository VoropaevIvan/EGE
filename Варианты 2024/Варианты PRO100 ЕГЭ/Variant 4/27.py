with open('27-B.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    a = [int(s) for s in file]

ans = -1
best_pref = -100000000000
for i in range(K, N):
    best_pref = max(best_pref, a[i-K] - (i-K))
    ans = max(ans, a[i] + best_pref + i)
print(ans)