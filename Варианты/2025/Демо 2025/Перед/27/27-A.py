cluster_A = [] # -0.5 1.5
cluster_B = [] # 3 5
with open('demo_2025_27_Б.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = [float(t) for t in s.split()]
        r_1 = (x - (-0.5))**2 + (y - 1.5)**2
        r_2 = (x - 3)**2 + (y - 5)**2
        if r_1 < r_2:
            cluster_A.append([x, y])
        else:
            cluster_B.append([x, y])

sum_A_x = sum([t[0] for t in cluster_A])
sum_A_y = sum([t[1] for t in cluster_A])
sum_A = sum([t[0]+t[1] for t in cluster_A])
sum_kv_A = sum([t[0]**2+t[1]**2 for t in cluster_A])

sum_B_x = sum([t[0] for t in cluster_B])
sum_B_y = sum([t[1] for t in cluster_B])
sum_B = sum([t[0]+t[1] for t in cluster_B])
sum_kv_B = sum([t[0]**2+t[1]**2 for t in cluster_B])

min_sum_A = 10**10
ans_A = [-1, -1]
for i in range(len(cluster_A)):
    x, y = cluster_A[i]
    sum_length = (len(cluster_A)-2)*(x**2+y**2) + sum_kv_A - 2*x*(sum_A_x - x) - 2*y*(sum_A_y - y)
    print(sum_length)
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
print(ans_A)
print(ans_B)
print((ans_A[0]+ans_B[0])/2*10_000//1)
print((ans_A[1]+ans_B[1])/2*10_000//1)
