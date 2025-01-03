import turtle
turtle.screensize(10000, 10000)
turtle.tracer(0)


def draw_cluster(cluster, color):
    for x, y in cluster:
        turtle.up()
        turtle.goto(x * k, y * k)
        turtle.down()
        turtle.dot(3, color)


def find_r(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def clustering(new_cluster):
    i = 0
    while i < len(new_cluster):
        for j in range(len(a)):
            if j not in used:
                x1, y1 = new_cluster[i]
                x2, y2 = a[j]
                if find_r(x1, y1, x2, y2) < e:
                    new_cluster.append(a[j])
                    used.add(j)
        i += 1
    return new_cluster


def find_centre(cluster):
    min_sum = 10 ** 10
    centre = [-1, -1]
    for x1, y1 in cluster:
        cur_sum = 0
        for x2, y2 in cluster:
            cur_sum += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        if cur_sum < min_sum:
            min_sum = cur_sum
            centre = [x1, y1]
    return centre



a = []
with open('files/27-31b.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = [float(t) for t in s.split()]
        a.append([x, y])

used = {0, 2, 4}
e = 0.2
k = 60

cluster_1 = clustering([a[0]])
cluster_2 = clustering([a[2]])
cluster_3 = clustering([a[4]])

# e = 1
# cluster_1 = clustering(cluster_1)
# cluster_2 = clustering(cluster_2)
# cluster_3 = clustering(cluster_3)

print('Рисую...')
draw_cluster(cluster_1, color='red')
draw_cluster(cluster_2, color='black')
draw_cluster(cluster_3, color='green')

print(len(cluster_1) + len(cluster_2) + len(cluster_3) == len(a))



centre_A = find_centre(cluster_1)
centre_B = find_centre(cluster_2)
centre_C = find_centre(cluster_3)
print(centre_A)
print(centre_B)
print(centre_C)
Px = (centre_A[0] + centre_B[0] + centre_C[0]) / 3
Py = (centre_A[1] + centre_B[1] + centre_C[1]) / 3
print(int(Px*100_000), int(Py*100_000))

turtle.done()