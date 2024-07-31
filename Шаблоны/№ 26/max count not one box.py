f = open('3_26.txt')
k = int(f.readline())
n = int(f.readline())

a = []
for s in f:
    a.append([int(x) for x in s.split()])

a.sort(key=lambda x: (x[1], -x[0]))

boxes = [-1]*k

count = 0
first = -1
last_nomer = -1
for x in a:
    start = x[0]
    end = x[1]
    boxes.sort(reverse=True)
    for i in range(k):
        if boxes[i] <= start:
            count += 1
            boxes[i] = end + 1
            if count == 1:
                first = end
            break


print(count, first)
f.close()
