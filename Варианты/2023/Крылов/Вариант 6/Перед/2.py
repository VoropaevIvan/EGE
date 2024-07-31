print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = y and (x <= w) and ((not x) <= ((not w) == z))
                if F == 0:
                    print(x, y, z, w, int(F))
