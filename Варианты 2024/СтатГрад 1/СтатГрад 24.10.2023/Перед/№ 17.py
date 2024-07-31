file = open('17.txt')
a = [int(s) for s in file]
osob = max([x for x in a if x % 100 == 19])

otvet = []
for i in range(0, len(a)-2):
    x = a[i]
    y = a[i+1]
    z = a[i+2]
    if (1000 <= x <= 9999) + (1000 <= y <= 9999) + (1000 <= z <= 9999) == 2:
        if (x % 3 == 0) + (y % 3 == 0) + (z % 3 == 0) >= 1:
            if x + y + z > osob:
                otvet.append(x + y + z)

print(len(otvet), max(otvet))

file.close()