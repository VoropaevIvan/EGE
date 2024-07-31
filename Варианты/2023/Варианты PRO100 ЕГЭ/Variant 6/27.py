with open('27-T.txt') as file:
    N, D = [int(x) for x in file.readline().split()]
    a = [int(x) for x in file]

count_2 = 0
L = 0
R = N - 1
while L < R:
    if a[L] + a[R] <= D:
        count_2 += 1
        L += 1
        R -= 1
    else:
        R -= 1

print(N - count_2)

