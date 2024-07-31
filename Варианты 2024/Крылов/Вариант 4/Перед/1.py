from itertools import *

table = '12 14 17 21 23 24 25 32 34 35 41 42 43 52 53 56 65 67 71 76'
graph = 'ab ba ac ca ad da db bd be eb cd dc de ed eg ge fg gf cf fc'

for per in permutations('abcdefg'):
    new_graph = table
    for i in range(1, 7+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)
        print()
