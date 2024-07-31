from fnmatch import fnmatch

for x in range(2024, 10**10, 2024):
    if fnmatch(str(x), '1?2*4'):
        if int(x**0.5)**2 == x:
            print(x, x//2024)