with open('17var06.txt') as file:
    a = [int(s) for s in file]

a_osob = [x for x in a if x % 2 == 0]
osob = max(a_osob)

otv = []
for i in range(0, len(a)-1):
    x, y = a[i], a[i+1]
    if x + y == osob:
        otv.append(x**2 + y**2)

print(len(otv), max(otv))
