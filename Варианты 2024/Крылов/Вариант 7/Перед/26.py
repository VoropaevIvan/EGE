with open('26var07.txt') as file:
    N, M = [int(x) for x in file.readline().split()]
    boxes = set()
    zamki = set()
    for i in range(M):
        box, zamok = [int(x) for x in file.readline().split()]
        boxes.add(box)
        zamki.add(zamok)
    for i in range(N-M):
        boxes.add(int(file.readline()))


ok_boxes = [x for x in boxes if x in zamki]
ok_boxes.sort(reverse=True)

last = 10**10
count = 0
for x in ok_boxes:
    if last - x >= 6:
        count += 1
        last = x
print(count, last)