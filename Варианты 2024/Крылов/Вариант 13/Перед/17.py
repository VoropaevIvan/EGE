with open('17var13.txt') as file:
    a = [int(s) for s in file]

otv = []
for i in range(0, len(a)-1):
    x, y = a[i], a[i+1]
    if (abs(x) % 10 == 5) and (abs(y) % 10 == 5):
        otv.append(abs(x - y))

print(len(otv), max(otv))
