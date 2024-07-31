from functools import *
@lru_cache(None)
def f(n):
    if n == 1:
        return 5
    if n > 1:
        return 2*n + 1 + f(n-1)

for i in range(2024, 1, -1):
    try:
        f(i)
    except:
        ...

for i in range(1, 2024):
    try:
        f(i)
    except:
        ...

print(f(2024) - f(2022))