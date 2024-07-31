from itertools import *

table = '12 17 21 23 25 26 32 34 36 37 43 45 46 52 54 56 62 63 64 65 71 73 78 87'
graph = 'аб ба бв вб бд дб гд дг аг га ге ег де ед дк кд ги иг еи ие ек ке ки ик'

for per in permutations('абвгдеки'):
    new_graph = table
    for i in range(1, 8+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8')
        print(*per)
        print()
