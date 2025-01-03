with open('reserv-B.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
a = ['*'] + a

pref = [0] * (N+1)
for i in range(1, N+1):
    pref[i] = pref[i-1] + a[i]

min_one = [10 ** 10] * (N + 1)
for i in range(0, N+1):
    min_one[i] = min(min_one[i - 1], pref[i])

max_two = [-10**10]*(N+1)
for i in range(2, N+1):
    max_two[i] = max(max_two[i-1], -min_one[i - 2] + pref[i])

max_three = [-10**10]*(N+1)
for i in range(3, N+1):
    max_three[i] = max(max_three[i-1], max_two[i-1] - pref[i])

ans = -1
for i in range(5, N+1):
    ans = max(ans, max_three[i-2] + pref[i])
print(ans)