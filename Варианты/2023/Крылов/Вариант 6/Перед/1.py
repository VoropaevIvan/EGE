from itertools import *

table = '13 15 26 27 31 35 45 47 51 53 54 56 62 65 72 74'
graph = 'аб ба бг гб аг га вг гв ве ев ек ке кд дк дг гд'

for per in permutations('абвгдек'):
    new_graph = table
    for i in range(1, 7+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)
        print()
