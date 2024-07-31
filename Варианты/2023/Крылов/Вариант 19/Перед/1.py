from itertools import *

table = '12 16 18 21 24 25 36 38 42 46 47 52 57 58 61 63 64 74 75 81 83 85'
graph = 'dc cd da ad cb bc ab ba ah ha bg gb hg gh he eh gf fg ef fe de ed'

for per in permutations('abcdefgh'):
    new_graph = table
    for i in range(1, 8+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8')
        print(*per)
        print()
