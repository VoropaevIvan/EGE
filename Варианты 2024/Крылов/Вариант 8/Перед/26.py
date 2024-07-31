with open('26var08.txt') as file:
    N, M = [int(x) for x in file.readline().split()]
    red_boxes = []
    blue_boxes = []
    for i in range(M):
        red_box, blue_box = [int(x) for x in file.readline().split()]
        red_boxes.append(red_box)
        blue_boxes.append(blue_box)
    for i in range(N - M):
        red_boxes.append(int(file.readline()))

red_boxes.sort(reverse=True)
blue_boxes.sort(reverse=True)

count = 0
last = 10 ** 10
i_b = -1
i_r = -1

# Поменять местами
while True:
    while True:
        i_b += 1
        if i_b == len(blue_boxes):
            print(count, last)
            exit()
        if last - blue_boxes[i_b] >= 5:
            last = blue_boxes[i_b]
            count += 1
            break
    while True:
        i_r += 1
        if i_r == len(red_boxes):
            print(count, last)
            exit()
        if last - red_boxes[i_r] >= 5:
            last = red_boxes[i_r]
            count += 1
            break
