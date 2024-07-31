from sys import *
from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n < 10:
        return 1
    return n + f(n - 1)


for i in range(1, 1_00_000 + 100):
    f(i)

print(f(100_000) - f(4141))
