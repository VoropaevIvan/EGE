# При регистрации в компьютерной системе каждому объекту сопоставляется идентификатор, состоящий из 15 символов
# и содержащий только символы из 8-символьного набора: А, В, C, D, Е, F, G, H. В базе данных для хранения сведений
# о каждом объекте отведено одинаковое и минимально возможное целое число байт. При этом используют посимвольное
# кодирование идентификаторов, все символы кодируют одинаковым и минимально возможным количеством бит.
# Кроме собственно идентификатора, для каждого объекта в системе хранятся дополнительные сведения,
# для чего отведено 24 байта на один объект.

# Определите объём памяти (в байтах), необходимый для хранения сведений о 20 объектах.
# В ответе запишите только целое число – количество байт.

from math import log2, ceil

# Дано
k = 15
N = 8
d_s = 24
count_obj = 20

# Решение
i = ceil(log2(N))
I = ceil(k * i / 8) + d_s

I_n = I * count_obj

print(f'i = {i} бит')
print(f'I = {I} байт')
print(I_n, 'байт')