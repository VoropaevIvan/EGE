file = open('27-A.txt')
k = int(file.readline())
a = [int(file.readline()) for s in range(int(file.readline()))]

ans = -1000000
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        for v in range(j + 1, len(a)):
            if v - i >= 3*k:
                ans = max(ans, a[i] + a[j] + a[v])
print(ans)

file.close()


