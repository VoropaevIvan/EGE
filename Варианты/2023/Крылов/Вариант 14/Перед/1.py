from itertools import *

table = '13 15 16 23 26 31 32 36 47 51 56 57 61 62 63 65 67 74 75 76'
graph = 'аб ба аг га бг гб бд дб гд дг дк кд гк кг ге ег ке ек ве ев'

for per in permutations('абвгдек'):
    new_graph = table
    for i in range(1, 7+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)
        print()
