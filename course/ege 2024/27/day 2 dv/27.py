with open('27-191a.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
a = ['*'] + a

pref = [0]*(N+1)
pref[1] = a[1]

max_pref_n = [-10**10, -1]
max_pref_c = [0, 0]
sum_ = 0

min_sum = 10**10
len_ = -1
for i in range(2, len(a)):
    pref[i] = pref[i-1] + a[i]
    if pref[i] % 2 == 0:
        ok_sum = pref[i] - max_pref_n[0]
        pos = max_pref_n[1]
    else:
        ok_sum = pref[i] - max_pref_c[0]
        pos = max_pref_c[1]

    if ok_sum == min_sum:
        len_ = max(len_, i - pos)
    elif ok_sum < min_sum:
        min_sum = ok_sum
        len_ = i - pos

    if pref[i-1] % 2 == 1 and pref[i-1] > max_pref_n[0]:
        max_pref_n = [pref[i-1], i-1]
    if pref[i-1] % 2 == 0 and pref[i-1] > max_pref_c[0]:
        max_pref_c = [pref[i-1], i-1]
print(len_)

