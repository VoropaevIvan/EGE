with open('r_27_A.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    a = ['*'] + [int(s) for s in file]


min_pref = [10**10]*(N+1)
min_pref[0] = 0
ans = -1000000000000
sum_ = 0
for i in range(1, N+1):
    sum_ += a[i]
    if i-K-1 >= 0:
        ans = max(ans, sum_ - min_pref[i-K-1])
    min_pref[i] = min(min_pref[i-1], sum_)
print(ans)