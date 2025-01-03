with open('reservdv-B.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
a = [-255, 278, -777, 820, 451]
N = 5
max_one = [-10 ** 10] * N
for i in range(0, N):
    max_one[i] = max(max_one[i - 1], -a[i])

max_two = [-10**10]*N
for i in range(1, N):
    max_two[i] = max(max_two[i-1], max_one[i - 1] + a[i])

max_three = [-10**10]*N
for i in range(2, N):
    max_three[i] = max(max_three[i-1], max_two[i-1] - a[i])

ans = -1
for i in range(3, N):
    ans = max(ans, max_three[i-1] + a[i])
print(ans)