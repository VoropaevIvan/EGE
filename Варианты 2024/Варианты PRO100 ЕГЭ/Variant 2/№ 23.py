from functools import *


@lru_cache(None)
def f(x, end):
    if x > end:
        return 0
    if x == end:
        return 1
    return f(x + 1, end) + f(x + 3, end) + f(x * 3, end)


print(f(3, 9) * f(9, 27) * f(27, 31))
