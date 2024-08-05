with open('peresdacha.txt') as file:
    N = int(file.readline())
    a = [int(s) for s in file]
a.sort(reverse=True)
print(sum(a[N//9:]))
ans_2 = 0
for i in range(N):
    if i % 9 != 8:
        ans_2 += a[i]
print(ans_2)