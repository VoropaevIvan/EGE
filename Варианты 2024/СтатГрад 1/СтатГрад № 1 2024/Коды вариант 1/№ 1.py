from itertools import *

table = '16 19 23 25 27 32 34 39 43 46 47 52 58 61 64 68 69 72 74 78 85 86 87 91 93 96'
graph = 'АБ БА БВ ВБ АВ ВА АГ ГА ГД ДГ ГЕ ЕГ ЕЖ ЖЕ ЖД ДЖ АИ ИА ВК КВ ИК КИ ИЕ ЕИ ЖК КЖ'

for per in permutations('АБВГДЕЖИК'):
    new_graph = table
    for i in range(1, 9+1):
        new_graph = new_graph.replace(str(i), per[i - 1])
    if set(new_graph.split()) == set(graph.split()):
        print(*per, sep='')