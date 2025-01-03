from solve_1 import *
from solve_2 import *
from solve_3 import *
from generate_tests import *
from gen_tests_numbers import *

for i in range(100_000):
    len_ = random.randint(1, 30)
    s = generate_s(len_)
    if solve_1(s) != solve_2(s):
        print()
        print('Ошибка')
        print(s)
        print(solve_1(s), solve_2(s))

print('Проверка завершена!')