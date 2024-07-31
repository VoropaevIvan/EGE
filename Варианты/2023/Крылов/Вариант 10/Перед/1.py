from itertools import *

table = '13 16 23 27 31 32 35 45 46 47 53 54 56 57 61 64 65 72 74 75'
graph = 'аб ба ав ва аг га дг гд ег ге бд дб ве ев дк кд ке ек кг гк'

for per in permutations('абвгдек'):
    new_graph = table
    for i in range(1, 7+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)
        print()
