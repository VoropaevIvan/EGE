def f(x):
    if x < 10:
        return x
    return x%10 + 8*f(x//10)


print(f(10**30))
print(int('1' + '0'*30, 8))
print(8**30)
