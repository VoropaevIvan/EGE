with open('27-A.txt') as file:
    n = int(file.readline())
    a = [int(s) for s in file]
otv = 0

for i in range(n):
    for j in range(i, n):
        c = 0
        for k in range(i, j + 1):
            if a[k] > 0:
                c += 1
            if a[k] < 0:
                c -= 1
        if c == 0:
            otv += 1
print(otv)
