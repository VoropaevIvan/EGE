def find_centre(cluster):
    min_sum = 10 ** 10
    centre = -1, -1
    for x1, y1 in cluster:
        cur_sum = 0
        for x2, y2 in cluster:
            cur_sum = cur_sum + ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        if cur_sum < min_sum:
            min_sum = cur_sum
            centre = x1, y1
    return centre


cluster_A = []
cluster_B = []
cluster_C = []
cluster_D = []
cluster_E = []
with open('files/27B.txt') as file:
    for s in file:
        x, y = [float(x) for x in s.replace(',', '.').split()]
        if x < 1 and y < 2:
            cluster_A.append([x, y])
        elif y > 3 and x < 3:
            cluster_B.append([x, y])
        elif y < 1 and x > 3:
            cluster_E.append([x, y])
        elif x > 3 and (1 <= y <= 5):
            cluster_D.append([x, y])
        elif x > 3 and (y > 5):
            cluster_C.append([x, y])
print(len(cluster_A))
print(len(cluster_B))
print(len(cluster_C))
print(len(cluster_D))
print(len(cluster_E))

centre_a = find_centre(cluster_A)
centre_b = find_centre(cluster_B)
centre_c = find_centre(cluster_C)
centre_d = find_centre(cluster_D)


px = (centre_a[0] + centre_b[0] + centre_c[0] + centre_d[0]) / 4 * 10_000
py = (centre_a[1] + centre_b[1] + centre_c[1] + centre_d[1]) / 4 * 10_000
print(int(px), int(py))
