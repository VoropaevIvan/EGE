with open('9.txt') as file:
    a = []
    d = [dict() for _ in range(5)]
    for s in file:
        a.append([int(x) for x in s.split()])
        for i in range(5):
            d[i][a[-1][i]] = d[i].get(a[-1][i], 0) + 1

for i in range(len(a)):
    row = a[i]
    c_u1 = [x % 2 == 0 for x in row]
    count_1 = 0
    for j in range(5):
        if sum(c_u1[j:]):
            count_1 += 1
    if count_1 >= 3 and any(row.count(row[j]) == d[j].get(row[j], 0) for j in range(5)):
        print(i+1)


