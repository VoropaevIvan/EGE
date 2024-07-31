with open('26t.txt') as file:
    a = []
    for s in file:
        start, len_ = [int(x) for x in s.split()]
        a.append([start, start+len_])

    #a = [[10, 20], [40, 50], [30, 60], [70, 80]]
    n = len(a)


a.sort(key=lambda x:x[1])

boxes_which_we_take = [a[0]]

for i in range(1, n):
    start_cur = a[i][0]
    end_cur = a[i][1]
    end_pred = boxes_which_we_take[-1][1]
    if end_pred <= start_cur:
        boxes_which_we_take.append([start_cur, end_cur])
print(len(boxes_which_we_take))

gran = boxes_which_we_take[-3][1]
ans_2 = -1
for i in range(0, n):
    for j in range(i+1, n):
        start_cur_1 = a[i][0]
        end_cur_1 = a[i][1]
        start_cur_2 = a[j][0]
        end_cur_2 = a[j][1]
        if gran <= start_cur_1 and end_cur_1 <= start_cur_2:
            ans_2 = max(ans_2, start_cur_2 - start_cur_1)
print(ans_2)
ans_3 = -1
gran = boxes_which_we_take[-2]
for i in range(n):
    start_cur = a[i][0]
    end_cur = a[i][1]
    if gran[1] <= start_cur:
        ans_3 = max(ans_3, start_cur - gran[0])
print(ans_3)


