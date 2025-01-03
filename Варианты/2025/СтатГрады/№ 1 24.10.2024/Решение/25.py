def find_dels(x):
    dels = []
    for d in range(2, int(x**0.5)+1):
        if x % d == 0:
            dels.append(d)
            if d != x // d:
                dels.append(x//d)
    return sorted(dels)

for x in range(110_250_000, 110_300_000 + 1):
    dels = find_dels(x)
    if len(dels) >= 2:
        m1, m2 = dels[-2:]
        if str(m1+m2)[-4:] == '1002':
            print(x)
