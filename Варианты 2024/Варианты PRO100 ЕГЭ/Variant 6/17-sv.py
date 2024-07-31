file = open('17.txt')
a = [int(x) for x in file]

osob = max([x for x in a if abs(x) % 1000 == 221])
ans = []
for i in range(len(a) - 2):
    x, y, z = a[i], a[i+1], a[i+2]
    if ((abs(x) // 10 % 10 % 2) != 0) + ((abs(y) // 10 % 10 % 2) != 0) + ((abs(z) // 10 % 10 % 2) != 0) == 2:
        if (9<abs(x)<100) + (9<abs(y)<100) + (9<abs(z)<100) <= 2:
            if x + y + z > osob:
                ans.append(x + y + z)
print(len(ans), min(ans))