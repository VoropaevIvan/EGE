with open('17var09.txt') as file:
    a = [int(s) for s in file]

otv = []
for i in range(0, len(a)-1):
    x, y = a[i], a[i+1]
    u1, u2 = False, False
    if x > 0:
        if int(x**0.5)**2 == x:
            u1 = True
    if y > 0:
        if int(y**0.5)**2 == y:
            u2 = True
    if u1 or u2:
        otv.append(x + y)

print(len(otv), max(otv))
