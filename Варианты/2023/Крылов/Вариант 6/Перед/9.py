count = 0
with open('9.txt') as file:
    for s in file:
        a = [int(x) for x in s.split()]
        a.sort()
        if 5*a[0] < (a[1] + a[2] + a[3]):
            if a[0] * a[3] == a[1] * a[2]:
                count += 1

print(count)