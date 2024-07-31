with open('18_d.txt') as file:
    a = [[int(x) for x in file.readline().split()] for i in range(20)]
    walls = [file.readline().split() for _ in range(20)]


d = [[100000] * 20 for _ in range(20)]
d[0][0] = a[0][0]
ans = 100000

for i in range(20):
    for j in range(20):
        if 'n' not in walls[i][j]:
            d[i + 1][j] = min(d[i + 1][j], d[i][j] + a[i + 1][j])
        if 'p' not in walls[i][j]:
            d[i][j + 1] = min(d[i][j + 1], d[i][j] + a[i][j + 1])
        if 'np' == walls[i][j]:
            ans = min(ans, d[i][j])

print(ans)