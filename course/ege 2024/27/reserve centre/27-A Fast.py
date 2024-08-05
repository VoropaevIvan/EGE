with open('test.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
ans = -1
for L1 in range(N):
    s1 = a[L1]
    for R1 in range(L1+1, N):
        s1 += a[R1]
        for L2 in range(R1 + 2, N):
            s2 = a[L2]
            for R2 in range(L2 + 1, N):
                s2 += a[R2]
                ans = max(ans, s1+s2)
print(ans)
