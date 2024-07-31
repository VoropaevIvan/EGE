with open('27-A.txt') as file:
    n = int(file.readline())
    a = [int(file.readline()) for _ in range(n)]
    b = [int(file.readline()) for _ in range(n)]

otv = 10**10
for i in range(n):
    for j in range(n):
        otv = min(otv, abs(a[i] - b[j]))
print(otv)
