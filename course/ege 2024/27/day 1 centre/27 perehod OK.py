with open('day1c-A.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]

a = ['*'] + a

pref = [0]*(N+1)
for i in range(1, N+1):
    pref[i] = pref[i-1] + a[i]

max_one = [-10 ** 10] * (N + 1)
max_one[0] = pref[0]
for i in range(1, N+1):
    max_one[i] = max(max_one[i-1], pref[i])

max_two = [-10 ** 10] * (N + 1)
for i in range(2, N+1):
    max_two[i] = max(max_two[i-1], max_one[i-2]-2*pref[i])

ans = -10**10
for i in range(4, N+1):
    ans = max(ans, max_two[i-2]+pref[i])
print(ans)


