with open('27-B.txt') as file:
    n = int(file.readline())
    a = [int(s) for s in file]


d = [0]*10**8
d[0] = 1
otv = 0
c = 0
for i in range(len(a)):
    if a[i] > 0:
        c += 1
    if a[i] < 0:
        c -= 1
    otv += d[c]
    d[c] += 1
print(otv)

