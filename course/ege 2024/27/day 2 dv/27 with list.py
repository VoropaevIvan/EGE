with open('27-191b.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
a = ['*'] + a

pref = [0]*(N+1)
for i in range(1, N+1):
    pref[i] = pref[i-1] + a[i]

max_pref_n = [[-10**10, -1] for _ in range(N+1)]
for i in range(1, N+1):
    if pref[i] % 2 == 1 and pref[i] > max_pref_n[i-1][0]:
        max_pref_n[i] = max(max_pref_n[i-1], [pref[i], i])
    else:
        max_pref_n[i] = max_pref_n[i - 1]

max_pref_c = [[-10**10, -1] for _ in range(N+1)]
max_pref_c[0] = [0, 0]
for i in range(1, N+1):
    if pref[i] % 2 == 0 and pref[i] > max_pref_c[i-1][0]:
        max_pref_c[i] = max(max_pref_c[i-1], [pref[i], i])
    else:
        max_pref_c[i] = max_pref_c[i - 1]


min_sum = 10**10
len_ = -1
for i in range(2, len(a)):
    if pref[i] % 2 == 0:
        ok_sum = pref[i] - max_pref_n[i-2][0]
        pos = max_pref_n[i-2][1]
    else:
        ok_sum = pref[i] - max_pref_c[i-2][0]
        pos = max_pref_c[i-2][1]

    if ok_sum == min_sum:
        len_ = max(len_, i - pos)
    elif ok_sum < min_sum:
        min_sum = ok_sum
        len_ = i - pos
print(len_)

