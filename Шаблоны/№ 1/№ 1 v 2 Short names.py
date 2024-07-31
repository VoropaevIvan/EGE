from itertools import *

t = '13 14 16 24 25 31 36 41 42 45 52 54 57 61 63 67 75 76'
g = 'df fd fa af ab ba bc cb ec ce ge eg de ed gd dg ca ac'

for per in permutations('abcdefg'):
    new_g = t
    for i in range(1, 8):
        new_g = new_g.replace(str(i), per[i - 1])
    if set(new_g.split()) == set(g.split()):
        print(*per)


