with open('27_B.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]

best_pref = 10**10
max_sum = -10**10
left_i = '*'
for i in range(1, N):
    if a[i-1] <= best_pref:
        best_pref = a[i-1]
        left_i = i-1
    if a[i] - best_pref >= max_sum:
        max_sum = a[i] - best_pref
        ans = i - left_i + 1
print(ans)