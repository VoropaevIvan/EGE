f = open('../Reserv/27_A.txt')
n = int(f.readline())
a = [int(x) for x in f]

otv = -1000000
for i in range(n):
    for j in range(i + 1, n):
        otv = max(otv, j-i + a[i] + a[j])
print(otv)
f.close()