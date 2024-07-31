with open('18.txt') as file:
    a = [[int(s) for s in file.readline().split()] for _ in range(20)]
    walls = [file.readline().split() for _ in range(20)]

d = [[100000000]*20 for _ in range(20)]
d[0][0] = a[0][0]
answers = []

for i in range(20):
    for j in range(20):
        if walls[i][j] == 's':
            continue
        if 'p' not in walls[i][j]:
            d[i][j+1] = min(d[i][j+1], d[i][j]+a[i][j+1])
        if 'n' not in walls[i][j]:
            d[i+1][j] = min(d[i+1][j], d[i][j]+a[i+1][j])
        if 'np' == walls[i][j]:
            answers.append(d[i][j])

print(min(answers), max(answers))

