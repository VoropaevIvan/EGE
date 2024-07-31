with open('17.txt') as file:
    a = [int(s) for s in file]

a_osob = [x for x in a if x % 100 == 13]
osob = max(a_osob)
otv = []
for i in range(0, len(a)-2):
    first = a[i]
    second = a[i+1]
    third = a[i+2]
    u1 = (first % 2 == 0) and (second % 2 == 0) and (third % 2 == 0)
    u2 = (10 <= first <= 99) or (10 <= second <= 99) or (10 <= third <= 99)
    if u1 or u2:
        if (first + second + third) <= osob:
            otv.append(first + second + third)

print(len(otv), sum(otv)//len(otv))
