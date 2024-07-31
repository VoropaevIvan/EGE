from itertools import *

table = '14 25 34 41 43 45 46 52 54 57 64 75'
graph = 'аб ба ав ва аг га гд дг ег ге гк кг'

for per in permutations('абвгдек'):
    new_graph = table
    for i in range(1, 7+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)
        print()
