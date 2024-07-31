from functools import *

@lru_cache(None)
def f(x, c):
    if c == 68:
        ans.add(x)
        return
    f(x+3, c+1)
    f(x-2, c+1)

ans = set()
f(1, 0)
print(len(ans))