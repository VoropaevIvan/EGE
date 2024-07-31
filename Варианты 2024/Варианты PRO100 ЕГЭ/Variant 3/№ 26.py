with open('D:\\IASV prod\\Шаблоны\\make_file\\26.txt') as file:
    n, k = [int(x) for x in file.readline().split()]
    levels = [[int(x) for x in s.split()] for s in file]

levels.sort()
count = 0
for i in range(n):
    if levels[i][0] <= k:
        k += levels[i][1]
        count += 1
    else:
        break
print(count, k)