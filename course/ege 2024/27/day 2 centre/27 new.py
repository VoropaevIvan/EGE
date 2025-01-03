with open('day2c-B.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
a = ['*'] + a

prefs = [[0, 0]]
sum_ = 0
for i in range(1, len(a)):
    sum_ += a[i]
    prefs.append([sum_, i])
prefs.sort(reverse=True)

max_len = -1
best_start = [10 ** 10, 10 ** 10]
best_start[prefs[0][0] % 2] = prefs[0][1]
for i in range(1, len(prefs)):
    best_len = prefs[i][1] - best_start[1 - prefs[i][0] % 2]
    max_len = max(max_len, best_len)
    best_start[prefs[i][0] % 2] = min(best_start[prefs[i][0] % 2], prefs[i][1])
print(max_len)
