with open('27v03_A.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    a = [int(s) for s in file]

min_one_pred = [10 ** 10] * N
min_two_pred = [10 ** 10] * N
min_three_pred = [10 ** 10] * N

min_one_pred[0] = a[0]
for i in range(1, N):
    min_one_pred[i] = min(min_one_pred[i - 1], a[i])

for i in range(K, N):
    min_two_pred[i] = min(min_two_pred[i - 1], a[i] * min_one_pred[i - K])

for i in range(2*K, N):
    min_three_pred[i] = min(min_three_pred[i - 1], a[i] * min_two_pred[i - K])

print(min_three_pred[-1])