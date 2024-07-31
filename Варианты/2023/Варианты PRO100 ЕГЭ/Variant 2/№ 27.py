with open('27-A.txt') as file:
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    b = [int(file.readline()) for _ in range(n)]

otv = 10**10
i = 0
j = 0
while i < n and j < n:
    otv = min(otv, abs(a[i] - b[j]))
    if a[i] < b[j]:
        i += 1
    else:
        j += 1
print(otv)



