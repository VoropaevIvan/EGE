from itertools import *

table = '12 13 14 15 16 17 21 27 31 35 37 41 45 46 51 53 54 61 64 71 72 73'
graph = 'ef fe fg gf ga ag ca ac cb bc bd db de ed ec ce cf fc cg gc cd dc'

for per in permutations('abcdefg'):
    new_graph = table
    for i in range(1, 7+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)
        print()