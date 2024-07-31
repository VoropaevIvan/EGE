from fnmatch import *


def prime(x):
    if x == 1:
        return 0
    for j in range(2, int(x ** 0.5) + 1):
        if x % j == 0:
            return 0
    return 1


for x in range(1, 10 ** 6 + 1):
    if fnmatch(str(x), '6868*7') and prime(x):
        print(x)
