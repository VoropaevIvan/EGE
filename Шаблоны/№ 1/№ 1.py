from itertools import *

table = '124 2146 356 41267 536 623457 746'
graf = 'абв бав вабдег две едвкг гвек кег'
table_d = {x[0]: set(x[1:]) for x in table.split()}
graf_d = {x[0]: set(x[1:]) for x in graf.split()}

for i in permutations('абвгдек'):
    d_new = {}
    for key, value in table_d.items():
        key_b = i[int(key) - 1]
        for x in value:
            d_new[key_b] = d_new.get(key_b, set())
            d_new[key_b].add(i[int(x) - 1])
    if d_new == graf_d:
        print('1 2 3 4 5 6 7')
        print(*i)
        print()

