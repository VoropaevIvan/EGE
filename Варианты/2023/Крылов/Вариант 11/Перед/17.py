with open('17var11.txt') as file:
    a = [int(s) for s in file]

otv = []
for i in range(0, len(a)-1):
    x, y = a[i], a[i+1]
    if (x % 3 == 0) and (y % 3 == 0):
        otv.append(x + y)

print(len(otv), max(otv))
