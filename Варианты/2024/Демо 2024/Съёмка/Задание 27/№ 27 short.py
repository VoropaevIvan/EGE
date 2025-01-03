file = open('27_B_2024.txt')
k = int(file.readline())
n = int(file.readline())
a = [int(s) for s in file]
file.close()

max_1 = [-10**10]*n
max_1[0] = a[0]
max_2 = [-10**10]*n
max_3 = [-10**10]*n

for i in range(1, len(a)):
    max_1[i] = max(max_1[i-1], a[i])
    if i >= k:
        max_2[i] = max(max_2[i-1], max_1[i-k] + a[i])
        max_3[i] = max(max_3[i-1], max_2[i-k] + a[i])

print(max_3[n-1])
