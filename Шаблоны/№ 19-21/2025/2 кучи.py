def f(x1, x2, c, win):
    if x1 + x2 >= 77:  # Указываем условие окончания игры
        return c in win
    if c > max(win):
        return 0
    # Записываем все возможные ходы
    moves = [f(x1 + 1, x2, c + 1, win), f(x1, x2 + 1, c + 1, win),
             f(x1 * 2, x2, c + 1, win), f(x1, x2 * 2, c + 1, win)]
    if c % 2 != max(win) % 2:
        return any(moves)  # Ходит наш игрок
    else:
        return all(moves)  # Ходит противник


for s in range(1, 69 + 1):  # Перебираем стартовое количество камней в куче
    if f(18, s, 0, [2]) == 1:
        print('№ 19:', s)
    if f(18, s, 0, [1]) == 0 and f(18, s, 0, [3]) == 1:
        print('№ 20:', s)
    if f(18, s, 0, [2, 4]) == 1 and f(18, s, 0, [2]) == 0:
        print('№ 21:', s)

# П1 В1 П2 В2
# 1  2  3  4