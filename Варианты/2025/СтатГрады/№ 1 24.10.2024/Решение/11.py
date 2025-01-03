from math import log2, ceil
for sp in range(0, 100000):
    N = 26+26+10+sp
    i = ceil(log2(N))
    k = 30
    if ceil(k*i/8)*4700 <= 180*1024:
        print(sp)