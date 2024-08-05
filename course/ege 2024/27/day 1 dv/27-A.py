with open('27-190a.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
ans = -10**10
for i in range(len(a)):
    for j in range(i+1, len(a)):
        for k in range(j+1, len(a)):
            if a[i] > a[j] and a[k] > a[j]:
                cur_sum = (a[i]-a[j]) + (a[k]-a[j])
                ans = max(ans, cur_sum)
print(ans)