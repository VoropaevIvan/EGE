with open('27v02_B.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    a = [int(s) for s in file]

max_one_pred = [-10**10]*N
max_two_pred = [-10**10]*N
max_three_pred = [-10**10]*N

max_one_pred[0] = a[0]
for i in range(1, N):
    max_one_pred[i] = max(max_one_pred[i-1], a[i])

for i in range(K, N):
    max_two_pred[i] = max(max_two_pred[i-1], a[i]+max_one_pred[i-K])

for i in range(2*K, N):
    max_three_pred[i] = max(max_three_pred[i-1], a[i]+max_two_pred[i-K])

print(max_three_pred[-1])