f = open('3_26.txt')
k = int(f.readline())
n = int(f.readline())
a = []
for s in f:
    a.append([int(x) for x in s.split()])

boxes = [[[-100, -1], [10 ** 6, 10 ** 6 + 1]] for _ in range(k)]

count = 0
last_nomer = -1
for x in a:
    start = x[0]
    end = x[1]
    vzyli = 0
    for i in range(k):
        if vzyli == 1:
            break
        for j in range(1, len(boxes[i])):
            if boxes[i][j - 1][1] <= start and end < boxes[i][j][0]:
                count += 1
                last_nomer = i + 1
                boxes[i].append([start, end+1])
                boxes[i].sort()
                vzyli = 1
                break

print(count, last_nomer)
# 383 199
