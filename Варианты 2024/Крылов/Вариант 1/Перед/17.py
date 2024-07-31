with open('17var01.txt') as file:
    a = [int(s) for s in file]

a_osob = [x for x in a if x % 100 == 25]
osob = min(a_osob)

otv = []
for i in range(0, len(a)-2):
    x, y, z = a[i], a[i+1], a[i+2]
    if (10 <= x <= 99) + (10 <= y <= 99) + (10 <= z <= 99) == 1:
        if x + y + z < osob:
            otv.append(x + y + z)

print(len(otv), max(otv))
