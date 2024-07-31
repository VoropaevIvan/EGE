from itertools import *

table = '12 13 15 17 21 24 26 27 31 36 37 42 45 48 51 54 62 63 67 71 72 73 76 84'
graph = 'аб ба бв вб бд дб гд дг аг га ге ег де ед дк кд ги иг еи ие ек ке ки ик'

for per in permutations('абвгдеки'):
    new_graph = table
    for i in range(1, 8+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8')
        print(*per)
        print()
