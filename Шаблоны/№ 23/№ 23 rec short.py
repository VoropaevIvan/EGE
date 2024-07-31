from functools import *
@lru_cache(None)
def f(x, end):
    if x == end:
        return 1
    if x > end:
        return 0
    if x == 17:
        return 0

    return f(x + 2, end) + f(x + 3, end) + f(x * 2, end)

print(f(3, 10) * f(10, 80))




