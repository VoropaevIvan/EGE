with open('17var05.txt') as file:
    a = [int(s) for s in file]

osob = max(a)

otv = []
for i in range(0, len(a)-1):
    x, y = a[i], a[i+1]
    if x + y == osob:
        otv.append(x**2 + y**2)

print(len(otv), max(otv))
