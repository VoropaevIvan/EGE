with open('26var05.txt') as file:
    n = int(file.readline())
    a = [int(s) for s in file]


a.sort(reverse=True)
last = 10 ** 10
count = 0
for x in a:
    if x <= last - 7:
        last = x
        count += 1
print(count, last)