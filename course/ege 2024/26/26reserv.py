# price, count_sell, count_have, virochka

with open('26reserv.txt') as file:
    N = int(file.readline())
    tovar = [[-1, 0, 0, 0] for _ in range(100_001)]
    prices = []
    for s in file:
        art, price, status = [int(x) for x in s.split()]
        count_sel = tovar[art][1]
        count_have = tovar[art][2]
        if status == 1:
            count_have += 1
        else:
            count_sel += 1
        tovar[art] = [price, count_sel, count_have, count_sel*price]
        prices.append(price)
price_gran = sum(prices) / len(prices)
primary_tovars = [x for x in tovar if x[0] > price_gran]
primary_tovars.sort(key=lambda x: [-x[1], -x[0], x[2]])
print(primary_tovars[0][3], primary_tovars[0][2])


