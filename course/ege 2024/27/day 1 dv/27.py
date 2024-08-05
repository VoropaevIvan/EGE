with open('27-190b.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]

max_left = [-10**10]*N
max_left[0] = a[0]
for i in range(1, N):
    max_left[i] = max(max_left[i-1], a[i])

max_right = [-10**10]*N
max_right[N-1] = a[N-1]
for i in range(N-2, -1, -1):
    max_right[i] = max(max_right[i+1], a[i])

ans = -10**10
for j in range(1, len(a)-1):
    left = max_left[j-1]
    right = max_right[j+1]
    if left > a[j] and right > a[j]:
        ans = max(ans, left+right-2*a[j])
print(ans)
