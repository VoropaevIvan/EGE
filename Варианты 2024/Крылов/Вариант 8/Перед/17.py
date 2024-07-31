with open('17var08.txt') as file:
    a = [int(s) for s in file]

osob = max(a)

otv = []
for i in range(0, len(a)-2):
    x, y, z = a[i], a[i+1], a[i+2]
    if (x % 10 != 3) and (y % 10 != 3) and (z % 10 != 3):
        if x**2 + y**2 + z**2 > osob:
            otv.append(x**2 + y**2 + z**2)

print(len(otv), min(otv))
