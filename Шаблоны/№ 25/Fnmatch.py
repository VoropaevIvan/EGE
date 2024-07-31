from fnmatch import *

for x in range(317, 10**8 + 1, 317):
    if fnmatch(str(x), '12??1*56'):
        print(x, x // 317)
