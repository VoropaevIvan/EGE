f = open('3_26_2t.txt')
n = int(f.readline())


a = []
for s in f:
    a.append([int(x) for x in s.split()])

a.sort(key=lambda x: x[1])

box_free = -1

count = 0
first = -1

for pas in a:
    start = pas[0]
    end = pas[1]
    if box_free == -1:
        first = end
    if box_free <= start:
        count += 1
        box_free = end + 1


print(count, first)
f.close()
