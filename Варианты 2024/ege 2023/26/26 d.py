with open('26_dt.txt') as file:
    n = int(file.readline())
    a = []
    for i in range(1, n+1):
        shlif, okr = [int(x) for x in file.readline().split()]
        a.append([shlif, -1, i])
        a.append([okr, 1, i])

a.sort()

used = set()
count_s = 0
count_o = 0

ans_1 = -1
ans_2 = -1

for x in a:
    time = x[0]
    type = x[1]
    id_ = x[2]
    if id_ in used:
        continue
    ans_1 = id_
    if type == -1:
        ans_2 = count_s
        count_s +=1
        used.add(id_)
    else:
        ans_2 = count_s
        count_o += 1
        used.add(id_)

print(ans_1, ans_2)