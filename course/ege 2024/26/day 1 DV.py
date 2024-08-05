with open('day1.txt') as file:
    N, count_ryd, count_nomer = [int(x) for x in file.readline().split()]
    a = []
    for s in file:
        ryd, mesto = [int(x) for x in s.split()]
        a.append([ryd, mesto])

for mesto in range(1, count_nomer+1):
    a.append([0, mesto])
    a.append([count_ryd + 1, mesto])

a.sort(key=lambda x:(x[1], x[0]))

max_free = -1
ans_ryd = -1
for i in range(1, len(a)):
    pred_ryd, pred_mesto = a[i-1]
    cur_ryd, cur_mesto = a[i]
    if pred_mesto == cur_mesto:
        cur_free = cur_ryd - pred_ryd - 2
        if cur_free > max_free:
            max_free = cur_free
            ans_ryd = cur_ryd - 1
        elif cur_free == max_free:
            ans_ryd = min(ans_ryd, cur_ryd - 1)
print(ans_ryd, max_free)

