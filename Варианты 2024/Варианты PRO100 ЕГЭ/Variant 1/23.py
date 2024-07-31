from functools import *


@lru_cache(None)
def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    if x == 100:
        return 0

    if x % 10 != 0:
        m1 = f(x + x % 10, end)
    else:
        m1 = 0
    if x % 68 != 0:
        m2 = f(x + x % 68, end)
    else:
        m2 = 0
    if x != 1:
        m3 = f(x * x, end)
    else:
        m3 = 0

    return m1 + m2 + m3


print(f(2, 68) * f(68, 500))
