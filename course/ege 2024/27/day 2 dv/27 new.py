with open('27-191a.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
a = ['*'] + a

pr = [0] * (N + 1)
for i in range(1, N + 1):
    pr[i] = pr[i - 1] + a[i]

max_pr = [-10 ** 10] * 2
max_pr[0] = 0
max_ind = [-1] * 2
max_ind[0] = 0

ans = 10**10
ans_d = 0

for r in range(1, N + 1):
    ost = 1 - pr[r]%2
    best = max_pr[ost]
    if pr[r] - best < ans:
        ans = pr[r] - best
        ans_d = r - max_ind[ost]
    elif pr[r] - best == ans:
        ans_d = max(ans_d, r - max_ind[ost])

    ost = pr[r - 1] % 2
    if pr[r - 1] > max_pr[ost]:
        max_pr[ost] = pr[r - 1]
        max_ind[ost] = r - 1
print(ans_d)
