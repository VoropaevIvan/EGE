count = 0
with open('9.txt') as file:
    for s in file:
        a = [int(x) for x in s.split()]
        a.sort()
        u1 = a[3]**2 > a[0] * a[1] * a[2]
        u2 = (a[1] - a[0]) == (a[2] - a[1]) == (a[3] - a[2])
        if u1 or u2:
            count += 1

print(count)