# ke 2184
# две версии универсального кода

f_usl = 1   # настраивается
a = 1   # настраивается
otr = []
for x in [0.5 * k for k in range(-1000000, 1000000)]:
    p = 1 <= x <= 39
    q = 23 <= x <= 58
    f = (p <= (not q)) <= (not a)
    if f == f_usl:  # настраивается
        if len(otr) == 0:
            otr.append(int(x))
        if x - otr[-1] > 0.5:
            print(int(otr[-1] + 0.5) - otr[0])
            otr = []
        else:
            otr.append(x)

print(int(otr[-1] + 0.5) - otr[0])






f_usl = 1  # настраивается
a = 1      # настраивается
px = '*'
for x in [0.5 * k for k in range(-1000000, 1000000)]:
    p = 1 <= x <= 39
    q = 23 <= x <= 58
    f = (p <= (not q)) <= (not a)
    if f == f_usl:   # настраивается
        if px == '*':
            begin = int(x)
            px = x
        elif x - px > 0.5:
            print(int(px + 0.5) - begin)
            px = '*'
        else:
            px = x
print(int(px + 0.5) - begin)
 
 
 
        
        
