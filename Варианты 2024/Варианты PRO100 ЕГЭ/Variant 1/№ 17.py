file = open('17.txt')
a = [int(s) for s in file]

ans = []
for i in range(0, len(a) - 3):
    first = a[i]
    second = a[i - 3]
    if (abs(first) % 100 == 13) + (abs(second) % 100 == 13) == 1:
        ans.append(first + second)
print(len(ans), min(ans))

file.close()
