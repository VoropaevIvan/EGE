from itertools import *

table = '15 16 17 19 23 24 26 29 32 34 39 42 43 51 59 61 62 67 68 71 76 78 86 87 91 92 93 95'
graph = 'ab ba ai ia bi ib bc cb ih hi be eb if fi ef fe cd dc gh hg de ed fg gf ce ec fh hf'

for per in permutations('abcdefghi'):
    new_graph = table
    for i in range(1, 9+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8 9')
        print(*per)
        print()
