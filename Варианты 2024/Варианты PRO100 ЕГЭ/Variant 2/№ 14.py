for x in range(1, 42141):
    a = 4*625**1920 + 4*125**x - 4*25**1940 - 3*5**1950 - 1960
    count_0 = 0
    #print(a)
    while a != 0:
        if (a % 5 == 0):
            count_0 += 1
        a //= 5
    if count_0 == 1891:
        print(x)
        break
    #print(count_0)

