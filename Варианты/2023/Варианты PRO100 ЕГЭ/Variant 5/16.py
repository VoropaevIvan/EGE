from functools import *


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return n * f(n - 1)


for i in range(1, 2023, 1):
    f(i)

print(f(2024) // f(2022))