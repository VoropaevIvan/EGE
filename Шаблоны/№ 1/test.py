from itertools import *

table = '12 14 21 23 25 32 35 36 41 45 47 52 53 54 63 67 74 76'
graph = 'db bd bc cb cg gc fg gf eg ge ef fe af fa ad da de ed'

for per in permutations('abcdefg'):
    new_graph = table
    for i in range(1, 7 + 1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)