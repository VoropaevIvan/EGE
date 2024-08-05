with open('test.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
a = ['*'] + a
max_len = -1
prefs = [[0, 0]]
sum_ = 0
for i in range(1, len(a)):
    sum_ += a[i]
    prefs.append([sum_, i])
prefs.sort(key=lambda x: [-x[0], -x[1]])
print(prefs)

best_start_c = 10**10
best_start_n = 10**10
if prefs[0][0] % 2 == 0:
    best_start_c = prefs[0][1]
else:
    best_start_n = prefs[0][1]

for i in range(1, len(prefs)):
    if prefs[i-1][0] != prefs[i][0]:
        if prefs[i][0] % 2 == 0:
            max_len = max(max_len, prefs[i][1] - best_start_n)
            best_start_c = min(best_start_c, prefs[i][1])
        else:
            max_len = max(max_len, prefs[i][1] - best_start_c)
            best_start_n = min(best_start_n, prefs[i][1])
    else:
        if prefs[i][0] % 2 == 0:
            best_start_c = min(best_start_c, prefs[i][1])
        else:
            best_start_n = min(best_start_n, prefs[i][1])
print(max_len)