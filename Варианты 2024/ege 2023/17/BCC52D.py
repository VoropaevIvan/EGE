file = open('308_17.txt')
a = [int(s) for s in file]
#a = a[1:]
osob = max(x for x in a if x % 100 == 13)
otv = []
for i in range(len(a)- 3):
    first = a[i]
    second = a[i+1]
    third = a[i+2]
    if (10 <= first <= 99) + (10 <= second <= 99) + (10 <= third <= 99) == 1:
        if (first + second + third) >= osob:
            otv.append(first + second + third)
print(len(otv), max(otv))
#257 197236
#257 197236