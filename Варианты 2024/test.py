mn = 1000000
mx = -1
for n in range(251, 1000):
    s = '5' * n
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '555', 1)

    c5 = s.count('5')
    if c5 <= mn:
        mn = c5
        o = max(mx, n)
print(o)