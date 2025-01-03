def find_centre(cluster):
    min_sum = 10**10
    centre = -1, -1
    for x1, y1 in cluster:
        cur_sum = 0
        for x2, y2 in cluster:
            cur_sum = cur_sum + ((x2-x1)**2 + (y2-y1)**2)**0.5
        if cur_sum < min_sum:
            min_sum = cur_sum
            centre = x1, y1
    return centre


cluster_A = []
cluster_B = []
cluster_C = []
with open('files/27A.txt') as file:
    for s in file:
        x, y = [float(x) for x in s.replace(',', '.').split()]
        if y < 2:
            cluster_A.append([x, y])
        elif y > 6:
            cluster_C.append([x, y])
        else:
            cluster_B.append([x, y])
print(len(cluster_A))
print(len(cluster_B))
print(len(cluster_C))
centre_b = find_centre(cluster_B)
centre_c = find_centre(cluster_C)
px = (centre_b[0]+centre_c[0])/2*10_000
py = (centre_b[1]+centre_c[1])/2*10_000
print(int(px), int(py))