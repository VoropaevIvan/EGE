file = open('17.txt')
a = [int(s) for s in file]

a_osob = [x for x in a if str(x)[-2:] == '19']
osob = max(a_osob)

ans = []
for i in range(0, len(a)-2):
    x = a[i]
    y = a[i+1]
    z = a[i+2]
    if (1000 <= x <= 9999) + (1000 <= y <= 9999) + (1000 <= z <= 9999) == 2:
        if (x % 3 == 0) or (y % 3 == 0) or (z % 3 == 0):
            if x + y + z > osob:
                ans.append(x + y + z)

print(len(ans), max(ans))
