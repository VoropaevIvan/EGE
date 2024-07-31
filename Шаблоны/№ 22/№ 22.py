f = open('files/22.csv')

d = {}
otv = {}
otv['0'] = 0
for s in f:
    s = s.replace('"', '')
    id_, time, zav = s.split()
    zav = zav.split(';')
    d[id_] = [int(time), zav]


def f(x):
    if x in otv:
        return otv[x]
    return max(f(x) for x in d[x][1]) + d[x][0]


# for x in otv:
#     otv[x] = f(x)

print(max(otv.values()))
f.close()
