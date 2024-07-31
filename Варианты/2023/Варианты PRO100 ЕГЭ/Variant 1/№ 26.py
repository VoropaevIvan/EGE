file = open('26t.txt')
n = int(file.readline())

films = [[int(x) for x in s.split()] for s in file]
ends = []
for start, end in films:
    ends.append([start, -1])
    ends.append([end, 1])
ends.sort()

c = 0
sum_ = 0
max_sum = -1
left = '-'
for i in range(len(ends)):
    time, type = ends[i]
    if type == -1:
        c += 1
        if c == 1:
            left = time
    if type == 1:
        c -= 1
        if c == 0:
            sum_ += time - left
            max_sum = max(max_sum, time - left)
print(sum_, max_sum)



file.close()