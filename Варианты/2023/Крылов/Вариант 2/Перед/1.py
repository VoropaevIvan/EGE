from itertools import *

table = '14 17 23 24 25 26 32 35 41 42 47 52 53 62 67 71 74 76'
graph = 'ab ba ae ea be eb bd db df fd ef fe fc cf fg gf gc cg'

for per in permutations('abcdefg'):
    new_graph = table
    for i in range(1, 7+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)
        print()
