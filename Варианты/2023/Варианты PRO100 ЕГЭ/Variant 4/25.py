from fnmatch import fnmatch

def is_prime(x):
    if x == 1:
        return False
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            return False
    return True

for x in range(1, 10**7+1):
    if fnmatch(str(x), '3?1111*'):
        if is_prime(x):
            print(x)
