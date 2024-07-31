from itertools import *

table = '13 14 16 24 25 31 36 41 42 45 52 54 57 61 63 67 75 76'
graph = 'df fd fa af ab ba bc cb ec ce ge eg de ed gd dg ca ac'

for per in permutations('abcdefg'):
    new_graph = table
    for i in range(1, 7+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)

