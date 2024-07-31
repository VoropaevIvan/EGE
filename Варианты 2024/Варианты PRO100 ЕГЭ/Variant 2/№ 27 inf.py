
n = int(input())
a = [int(s) for s in input().split()]
m = int(input())
b = [int(s) for s in input().split()]

otv = 10**10
i = 0
j = 0
while i < n and j < m:
    if abs(a[i] - b[j]) < otv:
        otv = min(otv, abs(a[i] - b[j]))
        otv_a = a[i]
        otv_b = b[j]
    if a[i] < b[j]:
        i += 1
    else:
        j += 1

print(otv_a, otv_b)



