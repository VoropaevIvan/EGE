import turtle

turtle.screensize(10000, 10000)
turtle.tracer(0)
k = 70

def draw_cluster(cluster, color):
    for x, y in cluster:
        turtle.up()
        turtle.goto(x * k, y * k)
        turtle.down()
        turtle.dot(10, color)


def find_r(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def find_centre(cluster):
    min_sum = 10 ** 10
    centre = [-1, -1]
    for x1, y1 in cluster:
        cur_sum = 0
        for x2, y2 in cluster:
            cur_sum += ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
        if cur_sum < min_sum:
            min_sum = cur_sum
            centre = [x1, y1]
    return centre


a = []
with open('files/demo_2025_27_Б.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = [float(t) for t in s.split()]
        a.append([x, y])

centres = [[0, 0],
           [3, 10],
           [4, 2]]

for _ in range(30):
    cl_x = [[], [], []]
    cl_y = [[], [], []]
    for x, y in a:
        r1 = find_r(x, y, centres[0][0], centres[0][1])
        r2 = find_r(x, y, centres[1][0], centres[1][1])
        r3 = find_r(x, y, centres[2][0], centres[2][1])

        if r1 <= r2 and r1 <= r3:
            cl_x[0].append(x)
            cl_y[0].append(y)
        elif r2 <= r1 and r2 <= r3:
            cl_x[1].append(x)
            cl_y[1].append(y)
        else:
            cl_x[2].append(x)
            cl_y[2].append(y)
    centres[0] = [sum(cl_x[0]) / len(cl_x[0]), sum(cl_y[0]) / len(cl_y[0])]
    centres[1] = [sum(cl_x[1]) / len(cl_x[1]), sum(cl_y[1]) / len(cl_y[1])]
    centres[2] = [sum(cl_x[2]) / len(cl_x[2]), sum(cl_y[2]) / len(cl_y[2])]

    # А зачем?
    #centres[0] = min(a, key=lambda x: find_r(x[0], x[1], centres[0][0], centres[0][1]))
    #centres[1] = min(a, key=lambda x: find_r(x[0], x[1], centres[1][0], centres[1][1]))
    #centres[2] = min(a, key=lambda x: find_r(x[0], x[1], centres[2][0], centres[2][1]))

cluster_A = tuple(zip(cl_x[0], cl_y[0]))
cluster_B = tuple(zip(cl_x[1], cl_y[1]))
cluster_C = tuple(zip(cl_x[2], cl_y[2]))

draw_cluster(cluster_A, 'red')
draw_cluster(cluster_B, 'black')
draw_cluster(cluster_C, 'green')

centre_A = find_centre(cluster_A)
centre_B = find_centre(cluster_B)
centre_C = find_centre(cluster_C)

# Px = (centre_A[0] + centre_B[0]) / 2
# Py = (centre_A[1] + centre_B[1]) / 2
Px = (centre_A[0] + centre_B[0] + centre_C[0]) / 3
Py = (centre_A[1] + centre_B[1] + centre_C[1]) / 3
print(int(Px * 10_000), int(Py * 10_000))

draw_cluster([centre_A, centre_B], 'green')
turtle.done()