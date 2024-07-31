with open('27_B_2024.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    a = [int(s) for s in file]

count_izm = 3
max_pred = [[-10*10]*N for _ in range(count_izm)]

max_pred[0][0] = a[0]
for i in range(1, N):
    max_pred[0][i] = max(max_pred[0][i - 1], a[i])
    for j in range(1, count_izm):
        if i >= j*K:
            max_pred[j][i] = max(max_pred[j][i - 1], a[i] + max_pred[j-1][i-K])

print(max_pred[-1][-1])