from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 3:
        return n
    if n > 2 and n % 2 == 1:
        return f(n-1) + f(n-2)
    if n > 2 and n % 2 == 0:
        sum_ = 0
        for i in range(1, (n-1)+1):
            sum_ += f(i)
        return sum_

print(f(38))