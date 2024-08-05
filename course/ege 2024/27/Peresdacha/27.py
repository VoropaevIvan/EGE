#?????
with open('peresdacha-B.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
a = ['*'] + a

pref = [0] * (N + 1)
for i in range(1, len(a)):
    pref[i] = pref[i - 1] + a[i]

min_pref = [10**10] * (N + 1)
min_pref[0] = 0
for i in range(1, len(a)):
    min_pref[i] = min(min_pref[i - 1], pref[i])

max_posl = [-10**10] * (N + 1)
for i in range(2, len(a)):
    max_posl[i] = max(max_posl[i - 1], pref[i] - min_pref[i-2])

max_pref_right = [-10**10] * (N + 1)
max_pref_right[N] = pref[N]
for i in range(N-1, 0, -1):
    max_pref_right[i] = max(max_pref_right[i+1], pref[i])

ans = -10**10
for i in range(4, len(a)-1):
    sum_ = max_posl[i-2] + (max_pref_right[i+1] - pref[i-1])
    ans = max(ans, sum_)
print(ans)
