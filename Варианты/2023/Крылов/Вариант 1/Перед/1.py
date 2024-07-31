from itertools import *

table = '14 15 17 23 25 27 32 35 41 47 51 52 53 56 65 67 71 72 74 76'
graph = 'ab ba ae ea be eb bc cb cd dc ed de ef fe fc cf fg gf gc cg'

for per in permutations('abcdefg'):
    new_graph = table
    for i in range(1, 7+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)
        print()


