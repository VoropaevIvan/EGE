with open('d2_27-A.txt') as file:
    N = int(file.readline())
    a = [int(s) for s in file]


ans = -10000000
for i in range(N):
    for j in range(i+1, N):
        ans = max(ans, a[i] + a[j] + j - i)
print(ans)