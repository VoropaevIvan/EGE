file = open('9.txt')
count = 0
for s in file:
    a = [int(x) for x in s.split()]
    if len(set(a)) == 6:
        a.sort()
        if (a[0]+a[-1])/2 < sum(a[1:-1])/4:
            count += 1
print(count)