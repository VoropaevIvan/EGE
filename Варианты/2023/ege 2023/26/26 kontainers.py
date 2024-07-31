with open('26_k.txt') as file:
    N, M = [int(x) for x in file.readline().split()]
    gruzy = [int(file.readline()) for _ in range(N)]
    konts = [int(file.readline()) for _ in range(M)]

gruzy.sort(reverse=True)
konts.sort(reverse=True)
count_g = 0
max_g = -1

uk_g = 0
uk_k = 0
while uk_g < N:
    if gruzy[uk_g] > konts[uk_k]:
        uk_g += 1
    else:
        uk_g += 1
        uk_k += 1
        count_g += 1
        max_g = max(max_g, gruzy[uk_g])

print(count_g, max_g)
