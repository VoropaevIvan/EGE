f = open('27_A_pr.txt')
n = int(f.readline())
a = [int(s) for s in f]
max_sum = -1
min_len = 10 ** 10

# Перебираем левый и правый конец подпоследовательности
for left in range(0, n):
    for right in range(left, n):
        sum_ = sum(a[left:right + 1])  # Считаем сумму чисел от left до right включительно
        if sum_ % 43 == 0:
            # Если встретили такую-же сумму, то выбираем минимальную длину между прошлой и текущей
            if max_sum == sum_:
                min_len = min(min_len, right - left + 1)

            # Если встретили бОльшую сумму, чем раньше, то запоминаем её
            if max_sum < sum_:
                max_sum = sum_
                min_len = right - left + 1  # Здесь просто обновляем, не ищем минимум
print(min_len)

f.close()
