from itertools import *

table = '124 2146 356 41267 536 623457 746'
graph = 'абв бав вабдег две едвкг гвек кег'
table = {int(x[0]) - 1: set(x[1:]) for x in table.split()}
graph = {x[0]: set(x[1:]) for x in graph.split()}

for per in permutations('абвдегк'):
    graph_new = table.copy()
    for old_key in set(graph_new):
        graph_new[per[old_key]] = {per[int(x) - 1] for x in graph_new.pop(old_key)}
    if graph_new == graph:
        print('1 2 3 4 5 6 7')
        print(*per)
        print()


