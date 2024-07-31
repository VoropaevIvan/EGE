f = open('27_B.txt')
n = int(f.readline())

a = []
for i in range(n):
    a.append([int(f.readline()), i])
a.sort(reverse=True)

otv = -10000
for i in range(10000):
    for j in range(i + 1, 10000):
        otv = max(otv, a[i][0] + a[j][0] + abs(a[i][1] - a[j][1]))

print(otv)
f.close()

# Правильно: 6231338
