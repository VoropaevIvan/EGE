from itertools import *

table = '1346 245 316 4125 5247 6137 756'
graf = 'gde dgef fda afbc bca ceba egcd'

graf_d = {x[0]: set(x[1:]) for x in graf.split()}

for per in permutations(graf_d):
    new_graf = table
    for i in range(1, 8):
        new_graf = new_graf.replace(str(i), per[i - 1])

    new_graf_d = {x[0]: set(x[1:]) for x in new_graf.split()}

    if new_graf_d == graf_d:
        print('1 2 3 4 5 6 7')
        print(*per)

