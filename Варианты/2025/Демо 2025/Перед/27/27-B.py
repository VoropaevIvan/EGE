cluster_A = [] # 1.5 1
cluster_B = [] # 3.5 9
cluster_C = [] # 6.8 5
with open('demo_2025_27_Б.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = [float(t) for t in s.split()]
        r_1 = (x - (1.5))**2 + (y - 1)**2
        r_2 = (x - 3.5)**2 + (y - 9)**2
        r_3 = (x - 6.8) ** 2 + (y - 5) ** 2
        if r_1 <= r_2 and r_1 <= r_3:
            cluster_A.append([x, y])
        if r_2 <= r_1 and r_2 <= r_3:
            cluster_B.append([x, y])
        if r_3 <= r_1 and r_3 <= r_2:
            cluster_C.append([x, y])

sum_A_x = sum([t[0] for t in cluster_A])
sum_A_y = sum([t[1] for t in cluster_A])
sum_A = sum([t[0]+t[1] for t in cluster_A])
sum_kv_A = sum([t[0]**2+t[1]**2 for t in cluster_A])

sum_B_x = sum([t[0] for t in cluster_B])
sum_B_y = sum([t[1] for t in cluster_B])
sum_B = sum([t[0]+t[1] for t in cluster_B])
sum_kv_B = sum([t[0]**2+t[1]**2 for t in cluster_B])

sum_C_x = sum([t[0] for t in cluster_C])
sum_C_y = sum([t[1] for t in cluster_C])
sum_C = sum([t[0]+t[1] for t in cluster_C])
sum_kv_C = sum([t[0]**2+t[1]**2 for t in cluster_C])

min_sum_A = 10**10
ans_A = [-1, -1]
for i in range(len(cluster_A)):
    x, y = cluster_A[i]
    sum_length = (len(cluster_A)-2)*(x**2+y**2) + sum_kv_A - 2*x*(sum_A_x - x) - 2*y*(sum_A_y - y)
    if sum_length < min_sum_A:
        min_sum_A = sum_length
        ans_A = [x, y]
print(ans_A)

min_sum_B = 10**10
ans_B = [-1, -1]
for i in range(len(cluster_B)):
    x, y = cluster_B[i]
    sum_length = (len(cluster_B)-2)*(x**2+y**2) + sum_kv_B - 2*x*(sum_B_x - x) - 2*y*(sum_B_y - y)
    if sum_length < min_sum_B:
        min_sum_B = sum_length
        ans_B = [x, y]

min_sum_C = 10**10
ans_C = [-1, -1]
for i in range(len(cluster_C)):
    x, y = cluster_C[i]
    sum_length = (len(cluster_C)-2)*(x**2+y**2) + sum_kv_C - 2*x*(sum_C_x - x) - 2*y*(sum_C_y - y)
    if sum_length < min_sum_C:
        min_sum_C = sum_length
        ans_C = [x, y]
print(ans_B)
print((ans_A[0]+ans_B[0]+ans_C[0])/3*10_000//1)
print((ans_A[1]+ans_B[1]+ans_C[1])/3*10_000//1)
