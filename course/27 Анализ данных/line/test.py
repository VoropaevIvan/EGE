a = []

for n in range(251, 1000):
    s = n * '5'
    while '55555' in s:
        s = s.replace('55555', '88', 1)
        s = s.replace('888', '555', 1)

    k = [s.count('5'), n]
    a.append(k)
a.sort()
print(a[:90])
