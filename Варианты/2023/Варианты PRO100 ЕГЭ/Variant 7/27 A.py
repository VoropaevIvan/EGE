with open('27_A.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
max_sum = -1000000
len_ = -1
for i1 in range(N):
    for i2 in range(i1, N):
        s = 0
        for k in range(i1+1, i2 + 1):
            s += (a[k] - a[k-1])
        if s >= max_sum:
            print(s, i1, i2)
            max_sum = s
#print(ans)
print(max_sum)
