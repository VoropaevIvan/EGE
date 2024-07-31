zvs = set()
for zv_1 in ['', '1', '3', '5', '7', '9']:
    for zv_2 in ['', '1', '3', '5', '7', '9']:
        for zv_3 in ['', '1', '3', '5', '7', '9']:
            zvs.add(zv_1+zv_2+zv_3)
answers = []
for vop in '02468':
    for zv in zvs:
        a = int('1' + vop + '2157' + zv + '4')
        if a % 133 == 0:
            answers.append([a, a // 133])
answers.sort()
for x in answers:
    print(x[0], x[1])