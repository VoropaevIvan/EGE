a = open('26-42.txt')
n, v = [int(x) for x in a.readline().split()]
A = []
Z = []
for x in a:
    if x.split()[0] == 'A':
        A.append(x.split()[1:])
    else:
        Z.append(x.split()[1:])
summ = 0
count = 0
A.sort(key=lambda x: int(x[0]))
print(A)
for x in Z:
    summ += int(x[0]) * int(x[1])
for x in A:
    if int(x[0]) * int(x[1]) + summ <= v:
        summ += int(x[0]) * int(x[1])
        count += int(x[1])
    else:
        count += ((v - summ) // int(x[0]))
        summ += ((v - summ) // int(x[0])) * int(x[0])
print(count)
print(v - summ)
