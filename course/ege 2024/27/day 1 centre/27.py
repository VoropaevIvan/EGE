with open('day1c-B.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
a = ['*'] + a

a_pref = [0]*(N+1)
a_pref[0] = 0
for i in range(1, N+1):
    a_pref[i] = a_pref[i-1] + a[i]

max_left = [-10**10]*(N+1)
max_left[0] = a_pref[0]
for i in range(1, N+1):
    max_left[i] = max(max_left[i-1], a_pref[i])

max_right = [-10**10]*(N+1)
max_right[N] = a_pref[N]
for i in range(N-1, -1, -1):
    max_right[i] = max(max_right[i+1], a_pref[i])

ans = -10**10
for i in range(3, N-1):
    sum_ = max_right[i+1] - 2*a_pref[i-1] + max_left[i-3]
    ans = max(ans, sum_)
print(ans)
