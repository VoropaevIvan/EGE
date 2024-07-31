with open('17var02.txt') as file:
    a = [int(s) for s in file]

a_osob = [x for x in a if x % 1000 == 100]
osob = max(a_osob)

otv = []
for i in range(0, len(a)-2):
    x, y, z = a[i], a[i+1], a[i+2]
    if (100 <= x <= 999) + (100 <= y <= 999) + (100 <= z <= 999) == 2:
        if x + y + z <= osob:
            otv.append(x + y + z)

print(len(otv), max(otv))
