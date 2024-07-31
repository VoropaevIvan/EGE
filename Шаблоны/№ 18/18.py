with open('18.txt', encoding='utf-8') as file:
    a = [[int(x) for x in file.readline().split()] for i in range(20)]
    walls = [file.readline().split() for _ in range(20)]

otv = [[100000] * 20 for _ in range(20)]
otv[0][0] = a[0][0]

for i in range(20):
    for j in range(20):
        if 'л' not in walls[i][j]:
            otv[i][j] = min(otv[i][j], otv[i][j - 1] + a[i][j])
        if 'в' not in walls[i][j]:
            otv[i][j] = min(otv[i][j], otv[i - 1][j] + a[i][j])

print(otv[19][19])



