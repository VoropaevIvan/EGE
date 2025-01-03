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
        return any(moves)  # Ходит противник

for s in range(1, 69 + 1):  # Перебираем стартовое количество камней в куче
    if f(7, s, 0, [2]) == 1:
        print('№ 19:', s)

# П1 В1 П2 В2
# 1  2  3  4