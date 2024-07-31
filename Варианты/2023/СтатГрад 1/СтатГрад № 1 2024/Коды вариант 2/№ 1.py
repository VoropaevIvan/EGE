from itertools import *

table = '14 19 25 27 37 38 39 41 45 46 52 54 57 58 64 68 69 72 73 75 83 85 86 91 93 96'
graph = 'АБ БА БВ ВБ АВ ВА АИ ИА АГ ГА ВК КВ ГД ДГ ГЕ ЕГ ДЖ ЖД ЕЖ ЖЕ ИЕ ЕИ ЖК КЖ ИК КИ'

for per in permutations('АБВГДЕЖИК'):
    new_graph = table
    for i in range(1, 9 + 1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(*per, sep='')