file = open('17_2024.txt')
a = [int(s) for s in file]
a = a[1:]
osob = max(x for x in a if abs(x) % 100 == 13)
otv = []
for i in range(len(a)- 3):
    first = a[i]
    second = a[i+1]
    third = a[i+2]
    if (100 <= abs(first) <= 999) + (100 <= abs(second) <= 999) + (100 <= abs(third) <= 999) == 2:
        if (first + second + third) <= osob:
            otv.append(first + second + third)
print(len(otv), max(otv))