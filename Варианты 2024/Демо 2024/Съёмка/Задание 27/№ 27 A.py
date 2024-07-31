file = open('27_A_2024.txt')
k = int(file.readline())
n = int(file.readline())
a = [int(s) for s in file]
file.close()

otv = -1000000000
for i1 in range(len(a)):
    for i2 in range(i1 + k, len(a)):
        for i3 in range(i2 + k, len(a)):
            sum_ = a[i1] + a[i2] + a[i3]
            otv = max(otv, sum_)
print(otv)
