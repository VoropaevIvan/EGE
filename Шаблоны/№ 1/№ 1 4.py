from itertools import *

table = '13 14 16 24 25 31 36 41 42 45 52 54 57 61 63 67 75 76'
graf = 'df fd fa af ab ba bc cb ec ce ge eg de ed gd dg ca ac'

for per in permutations('abcdefg'):
    new_graf = table.replace('1', per[0]).replace('2', per[1]).replace('3', per[2]).replace('4', per[3]).replace('5', per[4]).replace('6', per[5]).replace('7', per[6])
    if set(new_graf.split()) == set(graf.split()):
        print(*per)

