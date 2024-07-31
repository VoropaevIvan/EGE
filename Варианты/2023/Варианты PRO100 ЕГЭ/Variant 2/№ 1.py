from itertools import *

table = '12 15 21 25 26 34 35 43 45 47 51 52 53 54 56 57 62 65 67 74 75 76'
graph = 'аб ба бв вб вг гв гд дг де ед ек ке кд дк гк кг вк кв бк кб ак ка'

for per in permutations('абвгдек'):
    new_graph = table
    for i in range(1, 7 + 1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7')
        print(*per)

