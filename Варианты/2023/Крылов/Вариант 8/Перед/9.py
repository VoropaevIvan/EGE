count = 0
with open('9.txt') as file:
    for s in file:
        a = [int(x) for x in s.split()]
        a.sort()
        if a[0] ** 2 > a[1] + a[2] + a[3]:
            if (a[0] % 2 == 1) and (a[1] % 2 == 1) and (a[2] % 2 == 1) and (a[3] % 2 == 1):
                count += 1

print(count)


# if all(x % 2 == 1 for x in a):
