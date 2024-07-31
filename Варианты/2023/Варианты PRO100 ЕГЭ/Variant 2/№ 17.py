file = open("331_17.txt")
a = [int(s) for s in file]

a_osob = [x for x in a if str(abs(x))[0] == '8']
osob = max(a_osob)

otv = []
for i in range(0, len(a) - 2):
    first = a[i]
    second = a[i + 1]
    third = a[i + 2]
    if (str(abs(first))[0] == '6') + (str(abs(second))[0] == '6') + (str(abs(third))[0] == '6') <= 1:
        if first + second + third >= osob:
            otv.append(first + second + third)

print(len(otv), min(otv))


