from random import *

with open('24.txt', 'w') as file:
    n = 10 ** 7
    a = 'PRO'
    #print(n, m, file=file)
    for i in range(n):
        k = randint(0, 100)
        if k % 3 == 0:
            print('PRO', file=file, end='' )
        else:
            print(a[k%3], file=file, end='')

