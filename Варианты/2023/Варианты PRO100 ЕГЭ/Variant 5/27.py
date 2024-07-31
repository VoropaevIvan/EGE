with open('27-B.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    a = ['*']+[int(x) for x in file]
L, R = 1, 0
cur_sum, cur_count = 0, 0
max_count = 0
while True:
    if cur_sum < K:
        R += 1
        if R == N+1:
            break
        cur_count += 1
        cur_sum += a[R]
    else:
        L += 1
        cur_sum -= a[L-1]
        cur_count -= 1
    if cur_sum <= K:
        max_count = max(max_count, cur_count)
print(max_count)

