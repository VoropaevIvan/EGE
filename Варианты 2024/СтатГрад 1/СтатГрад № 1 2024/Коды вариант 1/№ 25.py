from fnmatch import *
for x in range(2024, 10**10+1, 2024):
    if fnmatch(str(x), '3?6906*4'):
        print(x)