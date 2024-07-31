with open('17var17.txt') as file:
    a = [int(s) for s in file]

otv = []
for i in range(0, len(a)-1):
    x, y = a[i], a[i+1]
    if x + y >= 100:
        if (x < 0) or (y < 0):
            otv.append(x*y)

print(len(otv), max(otv))
