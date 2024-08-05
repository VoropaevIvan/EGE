# A
with open('day1c-A.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]

ans = -10**10
for L in range(N):
    for M in range(L+1, N):
        for R in range(M+2, N):
            sum_ = sum(a[M+1:R+1]) - sum(a[L:M+1])
            ans = max(ans, sum_)
print(ans)