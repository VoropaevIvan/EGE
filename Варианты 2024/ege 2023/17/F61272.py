file = open('325_17.txt')
a = [int(s) for s in file]
a = a[1:]
osob = max(x for x in a if abs(x) % 100 == 19)
otv = []
for i in range(len(a)- 3):
    first = a[i]
    second = a[i+1]
    third = a[i+2]
    if (10 <= abs(first) <= 99) + (10 <= abs(second) <= 99) + (10 <= abs(third) <= 99) >= 1:
        if (first + second + third) < osob:
            otv.append(first + second + third)
print(len(otv), max(otv))
#3631 67430
#3631 67430