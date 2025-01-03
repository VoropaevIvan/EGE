with open('day1c-B.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]

a = ['*'] + a

pref = [0]*(N+1)
for i in range(1, N+1):
    pref[i] = pref[i-1] + a[i]

max_left = [-10**10]*(N+1)
max_left[0] = pref[0]
for i in range(1, N+1):
    max_left[i] = max(max_left[i-1], pref[i])

max_right = [-10**10]*(N+1)
max_right[N] = pref[N]
for i in range(N-1, -1, -1):
    max_right[i] = max(max_right[i+1], pref[i])

ans = -10**10
for j in range(2, N-2):
    left = max_left[j-2]
    right = max_right[j+2]
    ans = max(ans, left+right-2*pref[j])
print(ans)


