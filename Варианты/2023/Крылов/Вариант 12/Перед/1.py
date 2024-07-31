from itertools import *

table = '17 23 24 25 26 27 32 38 42 45 52 54 62 71 72 83'
graph = 'аг га гд дг дк кд кл лк лд дл дб бд де ед ев ве'

for per in permutations('абвгдекл'):
    new_graph = table
    for i in range(1, 8+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8')
        print(*per)
        print()
