with open('17var19.txt') as file:
    a = [int(s) for s in file]

otv = []
for i in range(0, len(a)-1):
    x, y = a[i], a[i+1]
    if (x > 700) or (y > 700):
        otv.append(x**2 + y**2)

print(len(otv), max(otv))
