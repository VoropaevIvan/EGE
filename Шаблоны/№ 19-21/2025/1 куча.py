def f(x, c, win):
    if x >= 68:  # Указываем условие окончания игры
        return c in win
    if c > max(win):
        return 0
    moves = [f(x + 1, c + 1, win), f(x * 3, c + 1, win)]  # Записываем все возможные ходы
    if c % 2 != max(win) % 2:
        return any(moves)  # Ходит наш игрок
    else:
        return all(moves)  # Ходит противник

for s in range(1, 67 + 1):  # Перебираем стартовое количество камней в куче
    if f(s, 0, [1]) == 0 and f(s, 0, [2]) == 1:
        print('№ 19:', s)
    if f(s, 0, [1]) == 0 and f(s, 0, [3]) == 1:
        print('№ 20:', s)
    if f(s, 0, [2, 4]) == 1 and f(s, 0, [2]) == 0:
        print('№ 21:', s)

# П1 В1 П2 В2
# 1  2  3  4