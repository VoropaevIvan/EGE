from random import *
from solve_1 import *
from solve_2 import *

with open('24.txt') as file:
    s = file.readline().strip()

for i in range(10000):
    l = randint(0, len(s)-10)
    r = randint(l, len(s)-5)
    a = s[l:r+1]
    if solve_1(a) != solve_2(a):
        print('Ошибка')
        print(a)
        print(solve_1(a), solve_2(a))

print('Проверка завершена!')