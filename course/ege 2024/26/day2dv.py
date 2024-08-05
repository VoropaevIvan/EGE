with open('test.txt') as file:
    N, K = [int(x) for x in file.readline().split()]
    a = []
    for s in file:
        rus, math, fiz = [int(x) for x in s.split()]
        a.append([rus+math+fiz, math, fiz, rus])
a.sort(reverse=True)
print(a[K-1][0], a[K-1][1])