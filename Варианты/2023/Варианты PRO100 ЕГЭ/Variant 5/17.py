with open('17.txt') as file:
    a = [int(s) for s in file]

fours = [a[i] + a[i + 1] + a[i + 2] + a[i + 3]
         for i in range(0, len(a) - 3)
         if len({abs(a[i]) % 10, abs(a[i+1]) % 10,abs(a[i+2]) % 10,abs(a[i+3]) % 10}) == 1]

max_osob = max([x for x in a if 10 <= abs(x) <= 99])
A = max(fours)

ans = []
for i in range(0, len(a) - 4):
    if (a[i] < A) + (a[i+1] < A) + (a[i+2] < A) + (a[i+3] < A) + (a[i+4] < A) == 1:
        if (a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4]) % max_osob == 0:
            ans.append(a[i]+a[i+1]+a[i+2]+a[i+3]+a[i+4])
print(len(ans), min(ans))


