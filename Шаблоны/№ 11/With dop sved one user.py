# При регистрации в компьютерной системе каждому пользователю выдаётся пароль, состоящий из 25 символов
# и содержащий только символы из 7-символьного набора: С, Д, А, М, Е, Г, Э. В базе данных для хранения сведений о
# каждом пользователе отведено одинаковое и минимально возможное целое число байт. При этом используют посимвольное
# кодирование паролей, все символы кодируют одинаковым и минимально возможным количеством бит. Кроме собственно пароля,
# для каждого пользователя в системе хранятся дополнительные сведения, для чего выделено целое число байт;
# это число одно и то же для всех пользователей. Для хранения сведений о 100 пользователях потребовалось 2400 байт.

# Сколько байт выделено для хранения дополнительных сведений об одном пользователе?
# В ответе запишите только целое число – количество байт.

from math import log2, ceil

# Дано
k = 25
N = 7
count_users = 100
I_n = 2400

# Решение
i = ceil(log2(N))
I = ceil(k * i / 8)

d_s = (I_n // count_users) - I

print(f'i = {i} бит')
print(f'I = {I} байт')
print('Ответ:', d_s, 'байт')