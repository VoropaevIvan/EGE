from itertools import *

table = '13 14 17 23 24 28 31 32 41 42 45 46 47 48 54 56 57 64 65 68 71 74 75 82 84 86'
graph = 'ab ba ag ga bh hb gh hg bc cb hf fh hc ch hd dh he eh de ed cd dc ef fe gf fg'

for per in permutations('abcdefgh'):
    new_graph = table
    for i in range(1, 8+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8')
        print(*per)
        print()
