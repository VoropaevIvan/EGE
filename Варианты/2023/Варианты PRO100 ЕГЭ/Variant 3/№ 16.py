# Неправильное решение
def F(n):
    return G(n - 1)


def G(n):
    if n < 10:
        return n
    return G(n - 2) + 1


count = 0
for n in range(1, 100 + 1):
    x = F(n)
    if int(x ** 0.5) ** 2 == x:
        count += 1
print(count)  # 13



