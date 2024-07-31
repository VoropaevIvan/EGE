f = open('17d.txt')
a = [int(s) for s in f]

a_osob = [x for x in a if abs(x) % 9 == 3]
osob = max(a_osob)
otv = []
for i in range(2, len(a)):
    first = a[i - 2]
    second = a[i - 1]
    third = a[i]
    u1 = (1000 <= abs(first) <= 9999) and (first % 2 == 0)
    u2 = (1000 <= abs(second) <= 9999) and (second % 2 == 0)
    u3 = (1000 <= abs(third) <= 9999) and (third % 2 == 0)
    if u1 + u2 + u3 <= 1:
        if (first + second + third) <= osob:
            otv.append(first + second + third)

print(len(otv), max(otv))
