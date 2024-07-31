with open('27_A_2024.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    a = [int(s) for s in file]

max_one_pred = [-10*10]*N
max_two_pred = [-10*10]*N
max_three_pred = [-10*10]*N

max_one_pred[0] = a[0]
for i in range(1, N):
    max_one_pred[i] = max(max_one_pred[i-1], a[i])
    if i >= K:
        max_two_pred[i] = max(max_two_pred[i - 1], a[i] + max_one_pred[i-K])
    if i >= 2*K:
        max_three_pred[i] = max(max_three_pred[i - 1], a[i] + max_two_pred[i-K])

print(max_three_pred[-1])