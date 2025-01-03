def f(cluster):
    sum_x = sum([t[0] for t in cluster])
    sum_y = sum([t[1] for t in cluster])
    sum_kv = sum([t[0] ** 2 + t[1] ** 2 for t in cluster])
    min_sum_lengths = 10 ** 10
    ans_pos = [-1, -1]
    for x, y in cluster:
        sum_length = (len(cluster)-2)*(x**2 + y**2) + sum_kv - 2*x*(sum_x - x) - 2*y*(sum_y - y)
        print(sum_length)
        if sum_length < min_sum_lengths:
            min_sum_lengths = sum_length
            ans_pos = [x, y]
    return ans_pos


cluster_A = [] # -0,6 1
cluster_B = [] # 1 4
cluster_C = [] # 6.8 5
with open('demo_2025_27_Б.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = [float(t) for t in s.split()]
        r_1 = (x - (1.5))**2 + (y - 1)**2
        r_2 = (x - 3.5)**2 + (y - 9)**2
        r_3 = (x - 6.8)**2 + (y - 5)**2
        if r_1 <= r_2 and r_1 <= r_3:
            cluster_A.append([x, y])
        if r_2 <= r_1 and r_2 <= r_3:
            cluster_B.append([x, y])
        if r_3 <= r_1 and r_3 <= r_2:
            cluster_C.append([x, y])

pos_A = f(cluster_A)
pos_B = f(cluster_B)
pos_C = f(cluster_C)

ans_1 = (pos_A[0] + pos_B[0] + pos_C[0])/3*10_000
ans_2 = (pos_A[1] + pos_B[1] + pos_C[1])/3*10_000
print(int(ans_1), int(ans_2))
