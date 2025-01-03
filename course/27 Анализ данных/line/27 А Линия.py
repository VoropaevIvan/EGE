def find_centre(cluster):  # Функция получает на вход кластер и возвращает его центр.
    min_sum = 10 ** 10  # Минимальная сумма расстояний от точки до всех остальных точек
    centre = [-1, -1]   # Центр кластера

    n = len(cluster)  # Количество точек в кластере
    sum_x = sum([x for x, y in cluster])  # Сумма кординат x всех точек: x1 + x2 + ... + xn
    sum_y = sum([y for x, y in cluster])  # Сумма кординат y всех точек: y1 + y2 + ... + yn
    # Сумма x^2 и y^2 всех точек: (x1^2 + x2^2 + ... + xn^2) + (y1^2 + y2^2 + ... + yn^2)
    sum_kv_x_y = sum([x**2 + y**2 for x, y in cluster])

    for x, y in cluster:  # Перебираем все точки кластера
        # Для текущей точки по формуле считаем сумму расстояний до всех других точек
        cur_sum = ((x**2+y**2) * n) + sum_kv_x_y - 2*x*sum_x - 2*y*sum_y
        if cur_sum < min_sum:  # Если сумма расстояний от текущей точки до всех других точек минимальна
            min_sum = cur_sum  # То запоминаем значение суммы растояний
            centre = [x, y]    # И координаты текущей точки
    return centre


# По графику видим, что есть два кластера.
cluster_A = []
cluster_B = []
with open('demo_2025_27_А (1).txt') as file:
    file.readline()
    for s in file:
        s = s.replace(',', '.')
        x, y = [float(t) for t in s.split()]
        if x <= 1:  # Разделяем точки на два кластера
            cluster_A.append([x, y])
        else:
            cluster_B.append([x, y])

centre_A = find_centre(cluster_A)  # Находим центр первого кластера
centre_B = find_centre(cluster_B)  # Находим центр второго кластера

# Вычисляем ответ
Px = (centre_A[0] + centre_B[0]) / 2
Py = (centre_A[1] + centre_B[1]) / 2
print(int(Px*10_000), int(Py*10_000))



