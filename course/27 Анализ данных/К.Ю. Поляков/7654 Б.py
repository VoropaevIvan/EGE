def find_centre(cluster):
    min_sum = 10 ** 10
    centre = [-1, -1]
    for x1, y1, h1 in cluster:
        cur_sum = 0
        for x2, y2, h2 in cluster:
            cur_sum += (((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5) * h2
        if cur_sum < min_sum:
            min_sum = cur_sum
            centre = [x1, y1]

    return centre


cluster_A = []
cluster_B = []
cluster_C = []
with open('../files/27-26b.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y, h = [float(t) for t in s.split()]
        if 50 <= x <= 210:
            cluster_A.append([x, y, h])
        elif -150 <= x <= 50 and y >= -25:
            cluster_B.append([x, y, h])
        elif x <= 0 and y <= -25:
            cluster_C.append([x, y, h])

centre_A = find_centre(cluster_A)
centre_B = find_centre(cluster_B)
centre_C = find_centre(cluster_C)
print(centre_A)
print(centre_B)
print(centre_C)
Px = (centre_A[0] + centre_B[0] + centre_C[0]) / 3
Py = (centre_A[1] + centre_B[1] + centre_C[1]) / 3
print(int(Px * 100_000), int(Py * 100_000))
