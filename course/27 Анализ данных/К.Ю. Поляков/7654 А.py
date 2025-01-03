def find_centre(cluster):
    min_sum = 10 ** 10
    centre = [-1, -1]
    for x1, y1, h1 in cluster:
        cur_sum = 0
        for x2, y2, h2 in cluster:
            cur_sum += (((x1 - x2)**2 + (y1 - y2)**2) ** 0.5) * h2
        if cur_sum < min_sum:
            min_sum = cur_sum
            centre = [x1, y1]
    return centre


cluster_A = []
cluster_B = []
with open('../files/27-26a.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y, h = [float(t) for t in s.split()]
        if x <= 180:
            cluster_A.append([x, y, h])
        elif x >= 310:
            cluster_B.append([x, y, h])


centre_A = find_centre(cluster_A)
centre_B = find_centre(cluster_B)
print(centre_A)
print(centre_B)
Px = (centre_A[0] + centre_B[0]) / 2
Py = (centre_A[1] + centre_B[1]) / 2
print(int(Px*100_000), int(Py*100_000))



