print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = x and (y <= z) and ((not y) <= ((not z) == w))
                if F == 0:
                    print(x, y, z, w, int(F))
