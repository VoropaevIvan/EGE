with open('17var12.txt') as file:
    a = [int(s) for s in file]

otv = []
for i in range(0, len(a)-1):
    x, y = a[i], a[i+1]
    if (x % 5 == 0) and (y % 5 == 0):
        otv.append(x + y)

print(len(otv), min(otv))
