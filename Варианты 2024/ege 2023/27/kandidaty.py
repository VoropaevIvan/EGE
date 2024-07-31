with open('27_A.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    a = ['*']+[int(s) for s in file]

r = N+1
ans = 0
count_in_pair = 0
for l in range(1, N+1):
    while r-1 >= 1 and a[l] + a[r-1] >= K:
        r -= 1
        count_in_pair += 1
    if l < r:
        ans += count_in_pair
    else:
        ans += (N - l)
print(ans)