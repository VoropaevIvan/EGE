def find_r(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


cluster_A = []
cluster_B = []
cluster_C = []
with open('../files/27-21b.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = [float(t) for t in s.split()]
        if 7.5 <= x <= 11:
            cluster_A.append([x, y])
        elif y > 5 and x < 5:
            cluster_B.append([x, y])
        elif 1 <= y <= 5 and 1 <= x <= 6:
            cluster_C.append([x, y])


d_min = 10**10
d_max = -10**10
for x1, y1 in cluster_A:
    for x2, y2 in cluster_B:
        r = find_r(x1, y1, x2, y2)
        d_min = min(d_min, r)
        d_max = max(d_max, r)
for x1, y1 in cluster_A:
    for x2, y2 in cluster_C:
        r = find_r(x1, y1, x2, y2)
        d_min = min(d_min, r)
        d_max = max(d_max, r)

for x1, y1 in cluster_B:
    for x2, y2 in cluster_C:
        r = find_r(x1, y1, x2, y2)
        d_min = min(d_min, r)
        d_max = max(d_max, r)
print(int(d_min*10_000), int(d_max*10_000))




