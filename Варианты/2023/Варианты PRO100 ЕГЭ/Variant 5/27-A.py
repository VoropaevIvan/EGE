with open('27-A.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    a = [int(x) for x in file]

ans = -1
for i in range(N):
    for j in range(i, N):
        sum_ = 0
        for q in range(i, j+1):
            sum_ += a[q]
        if sum_ <= K:
            ans = max(ans, j - i + 1)
print(ans)

