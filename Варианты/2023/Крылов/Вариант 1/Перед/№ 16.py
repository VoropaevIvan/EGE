from functools import *

@lru_cache(None)
def f(n):
    if n == 1:
        return 5
    if n > 1:
        return 2*n + 1 + f(n-1)

for i in range(1, 2000):
    f(i)

print(f(2024) - f(2022))