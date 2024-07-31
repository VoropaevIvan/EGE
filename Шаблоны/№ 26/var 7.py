f = open('3_26.txt')
k = int(f.readline())
n = int(f.readline())

a = []
for s in f:
    a.append([int(x) for x in s.split()])

a.sort()

boxes = [-1]*k

count = 0
first = -1
count_in_box = 0
last_in_box = -1
sum_in_box = 0
ends = []

for x in a:
    start = x[0]
    end = x[1]
    for i in range(k):
        if boxes[i] <= start:
            count += 1
            boxes[i] = end + 1
            if count == 1:
                first = end
            ends.append([start, 1])
            ends.append([end, -1])
            break

ends.sort()
for x in ends:
    if count_in_box > 0:
        sum_in_box += x[0] - last_in_box
    last_in_box = x[0]
    count_in_box += x[1]
    print(sum_in_box)

print(count, sum_in_box)
f.close()
