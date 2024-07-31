with open('27_kt2.txt') as file:
    K = int(file.readline())
    N = int(file.readline())
    a = ['*'] + [int(s) for s in file]

R = N + 1
count_pairs = 0
count_R = 0

for L in range(1, N + 1):
    while R > L and a[L] + a[R - 1] >= K:
        R -= 1
        count_R += 1
    if R == L:
        R += 1
        count_R -= 1
    count_pairs += count_R

print(count_pairs)
