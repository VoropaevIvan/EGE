def find_centre(cluster):
    min_sum = 10**10
    centre = [-1, -1]
    for i in range(len(cluster)):
        cur_sum = 0
        x1, y1 = cluster[i]
        for j in range(len(cluster)):
            x2, y2 = cluster[j]
            cur_sum += ((x1-x2)**2 + (y1-y2)**2) ** 0.5
        if cur_sum < min_sum:
            min_sum = cur_sum
            centre = [x1, y1]
    return centre


cluster_A = []
cluster_B = []
cluster_C = []
with open('demo_2025_27_А.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = [float(t) for t in s.split()]
        if x < 1:
            cluster_A.append([x, y])
        else:
            cluster_B.append([x, y])

pos_A = find_centre(cluster_A)
pos_B = find_centre(cluster_B)
#pos_C = find_centre(cluster_C)

ans_1 = (pos_A[0] + pos_B[0])/2*10_000
ans_2 = (pos_A[1] + pos_B[1])/2*10_000

# ans_1 = (pos_A[0] + pos_B[0] + pos_C[0])/3*10_000
# ans_2 = (pos_A[1] + pos_B[1] + pos_C[1])/3*10_000
print(int(ans_1), int(ans_2))
