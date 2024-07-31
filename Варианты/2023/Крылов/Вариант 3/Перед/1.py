from itertools import *

table = '15 16 24 25 36 37 42 45 47 51 52 54 56 61 63 65 73 74'
graph = 'ac ca ad da db bd be eb cd dc de ed eg ge fg gf cf fc'

for per in permutations('abcdefg'):
    new_graph = table
    for i in range(1, 7+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)
        print()
