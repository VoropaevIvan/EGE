with open('d2_27-B.txt') as file:
    N = int(file.readline())
    a = [int(s) for s in file]


best_pref = a[0] - 0
ans = -1000000000

for i in range(1, N):
    ans = max(ans, best_pref + a[i] + i)
    best_pref = max(best_pref, a[i] - i)
print(ans)