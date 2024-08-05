from solve_2 import *
from solve_3 import *
from generate_tests import *

for i in range(1000):
    len_ = random.randint(1, 80)
    s = generate(len_)
    if solve_2(s) != solve_3(s):
        print()
        print('Ошибка')
        print(s)
        print(solve_2(s), solve_3(s))

print('Проверка завершена!')