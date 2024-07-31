def check(l, r):
    for x in range(0, 300*3):
        a = l <= x <= r
        p = (9 * 3) <= x <= (19 * 3)
        q = (24 * 3) <= x <= (290 * 3)
        f = a <= (p or q)
        if f != f_usl:
            return 0
    return 1


otv = []
max_ = -1
f_usl = 1
for l in range(0, 300*3):
    for r in range(l, 300*3):
        if check(l, r) == 1:
            otv.append((r - l) / 3)

print(max(otv))
