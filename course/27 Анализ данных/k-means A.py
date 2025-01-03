def find_r(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5

a = []
with open('27-18a.txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = [float(t) for t in s.split()]
        a.append([x, y])

centres = [[2, 1],
           [4, 4]]

for _ in range(10):
    cl_1_x = []
    cl_1_y = []
    cl_2_x = []
    cl_2_y = []
    for x, y in a:
        r1 = find_r(x, y, centres[0][0], centres[0][1])
        r2 = find_r(x, y, centres[1][0], centres[1][1])
        if r1 <= r2:
            cl_1_x.append(x)
            cl_1_y.append(y)
        else:
            cl_2_x.append(x)
            cl_2_y.append(y)

    new_c_1 = [sum(cl_1_x)/len(cl_1_x), sum(cl_1_y)/len(cl_1_y)]
    new_c_2 = [sum(cl_2_x) / len(cl_2_x), sum(cl_2_y) / len(cl_2_y)]


    new_c_1 = min(a, key=lambda xt1: find_r(xt1[0], xt1[1], new_c_1[0], new_c_1[1]))
    new_c_2 = min(a, key=lambda xt2: find_r(xt2[0], xt2[1], new_c_2[0], new_c_2[1]))
    centres = [new_c_1[:], new_c_2[:]]

    print(min(a, key=lambda x: find_r(x[0], x[1], new_c_1[0], new_c_1[1])))
    print(min(a, key=lambda x: find_r(x[0], x[1], new_c_2[0], new_c_2[1])))
    print()



import turtle

# Данные точек
# Здесь, для примера, точки в трех кластерах
turtle.screensize(10000, 10000)

k = 40
# Настройка окна turtle
turtle.hideturtle()  # Скрываем курсор (черепаху)
turtle.bgcolor("white")  # Устанавливаем белый фон
turtle.tracer(0)
# Функция для отрисовки точки
def draw_point(x, y, color="blue"):
    turtle.penup()
    turtle.goto(x*k, y*k)
    turtle.pendown()
    turtle.dot(10, color)  # Рисуем точку диаметром 10 пикселей

# Отрисовка всех точек из данных
for point in zip(cl_1_x, cl_1_y):
    draw_point(point[0], point[1])

for point in zip(cl_2_x, cl_2_y):
    draw_point(point[0], point[1],color='red')

# Ожидание закрытия окна пользователем
turtle.done()
print(centres)
Px = (centres[0][0] + centres[1][0]) / 2
Py = (centres[0][1] + centres[1][1]) / 2
print(int(Px*10_000), int(Py*10_000))
