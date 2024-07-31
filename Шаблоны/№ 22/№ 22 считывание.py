def rec(id_):
    if id_ in otv:
        return otv[id_]
    return max(rec(x) for x in processes[id_][1]) + processes[id_][0]


processes, otv = {}, {'0': 0}
with open('files/22.csv') as f:
    for s in f:
        id_, time, zav = s.strip().split(',')
        processes[id_] = [int(time), zav.split(';')]

for x in processes:
    otv[x] = rec(x)

print(max(otv.values()))

print(max(rec(x) for x in processes))