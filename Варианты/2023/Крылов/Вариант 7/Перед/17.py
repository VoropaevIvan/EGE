with open('17var07.txt') as file:
    a = [int(s) for s in file]

osob = max(a)

otv = []
for i in range(0, len(a)-2):
    x, y, z = a[i], a[i+1], a[i+2]
    if (x % 10 == 0) + (y % 10 == 0) + (z % 10 == 0) == 1:
        if x + y + z < osob:
            otv.append(x + y + z)

print(len(otv), max(otv))
