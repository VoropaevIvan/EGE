def find_centre(cluster):
    min_sum = 10 ** 10
    centre = [-1, -1]
    for x1, y1 in cluster:
        cur_sum = 0
        for x2, y2 in cluster:
            cur_sum += abs(x1 - x2) + abs(y1 - y2)
        if cur_sum < min_sum:
            min_sum = cur_sum
            centre = [x1, y1]

    return centre


cluster_A = []
cluster_B = []
cluster_C = []
with open('../files/27-24b.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = [float(t) for t in s.split()]
        if y > -4:
            cluster_A.append([x, y])
        elif x < -3:
            cluster_B.append([x, y])
        else:
            cluster_C.append([x, y])

centre_A = find_centre(cluster_A)
centre_B = find_centre(cluster_B)
centre_C = find_centre(cluster_C)

Px = (centre_A[0] + centre_B[0] + centre_C[0]) / 3
Py = (centre_A[1] + centre_B[1] + centre_C[1]) / 3
print(int(Px * 10_000), int(Py * 10_000))

