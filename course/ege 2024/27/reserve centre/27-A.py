with open('reserv-A.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
ans = -1
for L1 in range(N):
    for R1 in range(L1+1, N):
        for L2 in range(R1 + 2, N):
            for R2 in range(L2 + 1, N):
                s1 = sum(a[L1:R1+1])
                s2 = sum(a[L2:R2+1])
                ans = max(ans, s1+s2)
print(ans)
