with open('17var20.txt') as file:
    a = [int(s) for s in file]

otv = []
for i in range(0, len(a)-1):
    x, y = a[i], a[i+1]
    if (x > 300) or (y > 300):
        otv.append(x**2 + y**2)

print(len(otv), min(otv))
