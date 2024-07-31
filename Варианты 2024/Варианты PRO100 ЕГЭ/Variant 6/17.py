with open('17.txt') as file:
    a = [int(x) for x in file]

max_221 = max([x for x in a if abs(x) % 1000 == 221])
ans = []
for i in range(0, len(a)-2):
    x, y, z = a[i], a[i+1], a[i+2]
    u1 = ((not(1 <= abs(x) <= 9)) and (abs(x) % 100 // 10 % 2 == 1)) + \
         ((not(1 <= abs(y) <= 9)) and (abs(y) % 100 // 10 % 2 == 1)) + \
         ((not(1 <= abs(z) <= 9)) and (abs(z) % 100 // 10 % 2 == 1))
    u2 = (10 <= abs(x) <= 99) + (10 <= abs(y) <= 99) + (10 <= abs(z) <= 99)

    if u1 == 2 and u2 <= 2 and (x + y + z) > max_221:
        ans.append(x + y + z)
print(len(ans), min(ans))
