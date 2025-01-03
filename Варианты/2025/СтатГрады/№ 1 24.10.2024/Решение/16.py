from sys import setrecursionlimit
setrecursionlimit(10000)
def f(n):
    if n < 3:
        return n
    return (n-1) * f(n-2)

a = (f(2025) - f(2023)) / f(2021)
print(a)