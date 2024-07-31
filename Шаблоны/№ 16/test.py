from functools import lru_cache


@lru_cache(None)
def f(n):
    if n == 10_000:
        return 1
    if n < 10_000:
        return n + f(n + 2)


for i in range(10_000, 10, -2):
    f(i)

print(f(1000) + f(10))
