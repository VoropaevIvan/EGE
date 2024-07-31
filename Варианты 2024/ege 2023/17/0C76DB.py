file = open('313_17.txt')
a = [int(s) for s in file]
a = a[1:]
osob = max(x for x in a if abs(x) % 100 == 15)
otv = []
for i in range(len(a)- 2):
    first = a[i]
    second = a[i+1]
    third = a[i+2]
    if (1000 <= abs(first) <= 9999) + (1000 <= abs(second) <= 9999) + (1000 <= abs(third) <= 9999) == 1:
        if (first + second + third) >= osob:
            otv.append(first + second + third)
print(len(otv), max(otv))
#299 196183
#299 196183