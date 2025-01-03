def find_centre(cluster):
    min_sum = 10 ** 10
    centre = [-1, -1]
    for x1, y1 in cluster:
        cur_sum = 0
        for x2, y2 in cluster:
            cur_sum += max(abs(x1 - x2), abs(y1 - y2))
        if cur_sum < min_sum:
            min_sum = cur_sum
            centre = [x1, y1]
    return centre


cluster_A = []
cluster_B = []
with open('../files/27-25a.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = [float(t) for t in s.split()]
        if x <= 2:
            cluster_A.append([x, y])
        else:
            cluster_B.append([x, y])

centre_A = find_centre(cluster_A)
centre_B = find_centre(cluster_B)

Px = (centre_A[0] + centre_B[0]) / 2
Py = (centre_A[1] + centre_B[1]) / 2
print(int(Px*10_000), int(Py*10_000))




