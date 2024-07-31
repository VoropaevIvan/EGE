with open('17var14.txt') as file:
    a = [int(s) for s in file]

otv = []
for i in range(0, len(a)-1):
    x, y = a[i], a[i+1]
    if (abs(x) % 10 == 7) and (abs(y) % 10 == 7):
        otv.append(abs(x - y))

print(len(otv), min(otv))
