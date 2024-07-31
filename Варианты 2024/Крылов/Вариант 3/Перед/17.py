with open('17var03.txt') as file:
    a = [int(s) for s in file]

a_osob = [x for x in a if abs(x) % 100 == 90]
osob = max(a_osob)

otv = []
for i in range(0, len(a)-2):
    x, y, z = a[i], a[i+1], a[i+2]
    if (1000 <= abs(x) <= 9999) + (1000 <= abs(y) <= 9999) + (1000 <= abs(z) <= 9999) >= 1:
        if x + y + z > osob:
            otv.append(x + y + z)

print(len(otv), min(otv))
