from functools import lru_cache


#@lru_cache(None)
def d(x):
    if x in finish:
        return x
    return processes[x][0] + max(d(y) for y in processes[x][1])


processes = {0: [0, []]}
with open('files/22_d.csv') as f:
    f.readline()
    for s in f:
        id_, time, zav = s.strip().split(',')
        processes[int(id_)] = [int(time), [int(x) for x in zav.split(';')]]

otv = set()
for i1 in range(20):
    for i2 in range(20):
        for i3 in range(20):
            for i4 in range(20):
                finish = {
                    0: 0,
                    1: i1 + processes[1][0],
                    2: i2 + processes[2][0],
                    9: i3 + processes[9][0],
                    10: i4 + processes[10][0]
                }
                life = [0] * 13
                for x in finish:
                    life[x] = [finish[x] - processes[x][0], finish[x]]
                # print(life)
                for i in range(1, 13):
                    if life[i] == 0:
                        life[i] = (d(i) - processes[i][0], d(i))

                otrs = []
                for start, end in life:
                    otrs.append([start, 1])
                    otrs.append([end, -1])

                otrs.sort()
                c = 0
                for t, type in otrs:
                    c += type
                    if c == 4:
                        left = t
                    if c == 3 and type == -1:
                        if (t - left) not in otv:
                            print(t - left)
                            otv.add(t - left)
