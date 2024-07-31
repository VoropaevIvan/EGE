with open('17var04.txt') as file:
    a = [int(s) for s in file]

a_osob = [x for x in a if abs(x) % 1000 == 700]
osob = min(a_osob)

otv = []
for i in range(0, len(a)-2):
    x, y, z = a[i], a[i+1], a[i+2]
    if (10000 <= abs(x) <= 99999) + (10000 <= abs(y) <= 99999) + (10000 <= abs(z) <= 99999) <= 2:
        if x + y + z >= osob:
            otv.append(x + y + z)

print(len(otv), min(otv))
