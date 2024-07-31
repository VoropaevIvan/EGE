from itertools import *

table = '12 21 23 25 27 28 32 38 47 52 56 65 72 74 82 83'
graph = 'аг га гд дг дк кд кл лк лд дл дб бд де ед ев ве'

for per in permutations('абвгдекл'):
    new_graph = table
    for i in range(1, 8+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8')
        print(*per)
        print()
