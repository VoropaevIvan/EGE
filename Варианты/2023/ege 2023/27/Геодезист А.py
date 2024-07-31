with open('r_27_A.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    a = [int(s) for s in file]

ans = -1
for i in range(0, N):
    for j in range(i+K, N):
        sum_ = 0
        for y in range(i, j+1):
            sum_ += a[y]
        ans = max(ans, sum_)
print(ans)