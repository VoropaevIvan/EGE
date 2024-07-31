print('a b c')
for a in range(2):
    for b in range(2):
        for c in range(2):
                f = ((b or b) <= c) == a
                if f == 1:
                    print(a, b, c)

