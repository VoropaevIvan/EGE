from itertools import *

table = '12 16 17 21 25 29 34 38 39 43 45 47 52 54 61 67 71 74 76 83 89 92 93 98'
graph = 'вг гв вл лв вм мв лм мл ем ме ед де гд дг аг га аб ба ак ка кб бк ек ке'

for per in permutations('лмевгдабк'):
    new_graph = table
    for i in range(1, 9+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8 9')
        print(*per)
        print()
