from functools import *

@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n**2 + f(n-1)

for i in range(1, 2023):
    f(i)

print(f(2023) - f(2019))