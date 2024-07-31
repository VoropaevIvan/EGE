with open('17var15.txt') as file:
    a = [int(s) for s in file]

otv = []
for i in range(0, len(a)-1):
    x, y = a[i], a[i+1]
    if abs(x) % 10 == abs(y) % 10:
        if abs(x) % 2 == 1:
            otv.append(abs(x)*abs(y))

print(len(otv), max(otv))
