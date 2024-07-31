file = open('26.txt')
n = int(file.readline())

a = [[int(x) for x in s.split()] for s in file]
a.sort()
most_late_start = a[-1][0]
a.sort(key=lambda x: x[1])

last = [-1]
count = 0
ans_2 = -1
for i in range(n):
    if last[-1] <= a[i][0]:
        count += 1
        last.append(a[i][1] + 20)
    ans_2 = most_late_start - last[-2] + 20

print(count, ans_2)










file.close()