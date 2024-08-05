with open('test.txt') as file:
    N = int(file.readline())
    a = [int(x) for x in file]
a = ['*'] + a

min_left = [10**10]*(N+1)
for i in range(1, len(a)):
    min_left[i] = min(min_left[i-1], a[i])

max_two = [-10**10]*(N+1)
for i in range(2, N+1):
    max_two[i] = max(max_two[i-1], a[i]-min_left[i-1])

max_right = [-10**10]*(N+1)
max_right[N] = a[N]
for i in range(N-1, 0, -1):
    max_right[i] = max(max_right[i+1], a[i])

ans = -1
for k in range(3, len(a)-1):
    sum_ = max_two[k-1] - a[k] + max_right[k+1]
    ans = max(ans, sum_)
print(ans)