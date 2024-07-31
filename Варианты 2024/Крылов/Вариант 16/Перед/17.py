with open('17var16.txt') as file:
    a = [int(s) for s in file]

otv = []
for i in range(0, len(a)-1):
    x, y = a[i], a[i+1]
    if (abs(x) % 2 == 1) and (abs(y) % 2 == 1):
        if abs(x) % 10 != abs(y) % 10:
            otv.append(abs(x)*abs(y))

print(len(otv), min(otv))
