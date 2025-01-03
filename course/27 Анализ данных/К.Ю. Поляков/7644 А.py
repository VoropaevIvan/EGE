import turtle
turtle.screensize(10000, 10000)
turtle.tracer(0)


def draw_cluster(cluster, color):
    for x, y in cluster:
        turtle.up()
        turtle.goto(x * k, y * k)
        turtle.down()
        turtle.dot(6, color)


def find_r(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def clustering(new_cluster):
    i = 0
    while i < len(new_cluster):
        for j in range(len(a)):
            if j not in used:
                x1, y1 = new_cluster[i]
                x2, y2 = a[j]
                if find_r(x1, y1, x2, y2) <= e:
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
with open('../files/27-22a.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = [float(t) for t in s.split()]
        a.append([x, y])

used = {0, 3}
e = 1
k = 60

cluster_1 = clustering([a[0]])
cluster_2 = clustering([a[3]])


print('Рисую...')
draw_cluster(cluster_1, color='red')
draw_cluster(cluster_2, color='black')


print(len(cluster_1) + len(cluster_2), len(a))
print(len(cluster_1) + len(cluster_2) == len(a))



centre_A = find_centre(cluster_1)
centre_B = find_centre(cluster_2)

print(centre_A)
print(centre_B)

Px = (centre_A[0] + centre_B[0]) / 2
Py = (centre_A[1] + centre_B[1]) / 2
print(int(Px*100_000), int(Py*100_000))


draw_cluster([centre_A, centre_B], color='green')
turtle.done()