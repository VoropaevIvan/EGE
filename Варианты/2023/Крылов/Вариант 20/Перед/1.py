from itertools import *

table = '12 13 14 21 24 28 31 35 37 41 42 45 46 47 48 53 54 56 57 64 65 68 73 74 75 82 84 86'
graph = 'ab ba ag ga ac ca bh hb hg gh gf fg cd dc de ed fe ef eh he dh hd hf fh gb bg hc ch'

for per in permutations('abcdefgh'):
    new_graph = table
    for i in range(1, 8+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8')
        print(*per)
        print()
