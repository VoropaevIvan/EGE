from itertools import *

table = '12 16 21 25 26 35 37 38 45 49 52 53 54 61 62 69 73 78 83 87 89 94 96 98'
graph = 'вг гв вл лв вм мв лм мл ем ме ед де гд дг аг га аб ба ак ка кб бк ек ке'

for per in permutations('лмевгдабк'):
    new_graph = table
    for i in range(1, 9+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print('1 2 3 4 5 6 7 8 9')
        print(*per)
        print()
